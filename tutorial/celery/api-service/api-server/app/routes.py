from flask import url_for, jsonify, request
from datetime import datetime

from app import app, db
from app.models import User, Task, TaskStatus, TestTask, CodeCoverageTask, \
    TaskMsg, Result
from app.util import try_commit

from worker.app import celery
from worker.app.test.tasks import long_add
from worker.app.code_coverage.tasks import code_coverage_task


URI_API = '/api'


def link(link):
    return "<a href='{0}'>{0}</a></br>".format(link)


@app.route(URI_API)
def index():
    host = 'http://{HOST}'.format(HOST=app.config['PUBLIC_IP'])
    if app.config['PORT'] != 80:
        host += ':{PORT}'.format(PORT=app.config['PORT'])
    return ("Refer to repo: {0}".format(link("https://gitswarm.companynet.com/secauto/api-service")) # noqa
          + "Refer to api doc: {0}".format(link("https://secauto.pages.gitswarm.companynet.com/api-service-api-doc-page")) # noqa
          + "<br>==user==</br>" # noqa
          + link(host+URI_API+'/user') # noqa
          + link(host+URI_API+'/user/:user_id') # noqa
          + "<br>==task==</br>" # noqa
          + link(host+URI_API+'/task') # noqa
          + link(host+URI_API+'/task/:task_id') # noqa
          + link(host+URI_API+'/task/result/:future_result_id') # noqa
          + "<br>==test task==</br>" # noqa
          + link(host+URI_API+'/task/test') # noqa
          + link(host+URI_API+'/task/test/:task_id') # noqa
          + "<br>==code coverage task==</br>" # noqa
          + link(host+URI_API+'/task/code-coverage') # noqa
          + link(host+URI_API+'/task/code-coverage/:task_id') # noqa
    )


# == user ==
@app.route(URI_API+'/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        users = User.query.all()
        response = {
            'users': [user.to_dict() for user in users],
            'total': len(users)
        }
        return jsonify(response)
    elif request.method == 'POST':
        payload = request.get_json()
        app.logger.debug('request payload: %s', payload)

        name = payload['name']
        email = payload['email']

        user = User(
            name=name,
            email=email,
        )
        db.session.add(user)
        try_commit(db.session)

        user.selflink = 'http://localhost' + url_for('user_info', user_id=user.id) # noqa
        db.session.add(user)
        try_commit(db.session)

        response = {
            'status': '%s created successfully!' % user,
            'name': name,
            'email': email,
        }
        return jsonify(response)


@app.route(URI_API+'/user/<user_id>', methods=['GET'])
def user_info(user_id):
    user = User.query.filter_by(id=user_id).first()
    response = user.to_dict()
    return jsonify(response)


# == task ==
@app.route(URI_API+'/task', methods=['GET'])
def task():
    tasks = Task.query.all()
    response = {
        'tasks': [super(task.__class__, task).to_dict() for task in tasks],
        'total': len(tasks)
    }
    return jsonify(response)


@app.route(URI_API+'/task/result/<future_result_id>', methods=['GET'])
def task_result(future_result_id):
    future_result = celery.AsyncResult(future_result_id)
    if future_result.state == 'FAILURE':
        response = {
            'task_selflink': Task.get_task_by_future_result_id(future_result.id).selflink, # noqa
            'state': future_result.state,
            'error': str(future_result.info)  # when exception raised
        }
    else:
        response = {
            'task_selflink': Task.get_task_by_future_result_id(future_result.id).selflink, # noqa
            'state': future_result.state,
            'result': future_result.info
        }
    return jsonify(response)


@app.route(URI_API+'/task/<task_id>', methods=['GET'])
def task_info(task_id):
    task = Task.query.filter_by(id=task_id).first()
    response = super(task.__class__, task).to_dict()
    response.update({
        'messages': [repr(task_msg) for task_msg in TaskMsg.get_msgs_by_task_id(task_id)] # noqa
    })
    return jsonify(response)


# == task - test ==
@app.route(URI_API+'/task/test', methods=['GET', 'POST'])
def task_test():
    if request.method == 'GET':
        tasks = Task.query.filter_by(type='test_task').all()
        response = {
            'tasks': [task.to_dict() for task in tasks],
            'total': len(tasks)
        }
        return jsonify(response)
    elif request.method == 'POST':
        payload = request.get_json()
        app.logger.debug('request payload: %s', payload)

        # validate payload
        ok, err_msg = TestTask.validate(payload)
        if not ok:
            response = {
                'error': err_msg # noqa
            }
            return jsonify(response), 400

        # unload payload
        task_name = payload['name']
        user_name = payload['user']
        priority = payload.get('priority', 0)
        data = payload['data']
        a = data['a']
        b = data['b']

        # persist to db
        user = User.get_user_by_name(name=user_name)
        if not user:
            email = payload.get('email', '%s@company.com' % user_name)
            user = User(name=user_name, email=email)
        user.last_login = datetime.now()

        task = TestTask(
            status=TaskStatus.RECEIVED,
            type='test_task',
            name=task_name,
            user=user,
            priority=priority,
            a=a,
            b=b,
        )
        db.session.add(task)
        try_commit(db.session)

        task.selflink = 'http://localhost' + url_for('task_info', task_id=task.id) # noqa
        db.session.add(task)
        try_commit(db.session)

        db.session.add(
            TaskMsg(task_id=task.id, msg="Received request for task %s." % task) # noqa
        )
        try_commit(db.session)

        # schedule task on worker
        future_result = long_add.apply_async(
            (task.id, a, b),
            queue='test'
        )

        # persist to db
        result = Result(
            id=future_result.id,
            selflink = 'http://localhost' + url_for('task_result', future_result_id=future_result.id) # noqa
        )
        db.session.add(result)
        try_commit(db.session)

        task.status = TaskStatus.SCHEDULED
        task.future_result_id = future_result.id
        db.session.add(task)
        try_commit(db.session)

        db.session.add(
            TaskMsg(task_id=task.id, msg="Scheduled task %s." % task)
        )
        try_commit(db.session)

        response = {
            'selflink': task.selflink,
            'resultlink': result.selflink
        }
        return (jsonify(response),
               202,
               {'Location': url_for('task_result', future_result_id=future_result.id)}) # noqa


@app.route(URI_API+'/task/test/<task_id>', methods=['GET'])
def task_test_info(task_id):
    task = Task.query.filter_by(id=task_id).first()
    response = task.to_dict()
    response.update({
        'messages': [repr(task_msg) for task_msg in TaskMsg.get_msgs_by_task_id(task_id)] # noqa
    })
    return jsonify(response)


# == task - code coverage ==
@app.route(URI_API+'/task/code-coverage', methods=['GET', 'POST'])
def task_code_coverage():
    if request.method == 'GET':
        tasks = Task.query.filter_by(type='code_coverage_task').all()
        response = {
            'tasks': [task.to_dict() for task in tasks],
            'total': len(tasks)
        }
        return jsonify(response)
    elif request.method == 'POST':
        payload = request.get_json()
        app.logger.debug('request payload: %s', payload)

        # validate payload
        ok, err_msg = CodeCoverageTask.validate(payload)
        if not ok:
            response = {
                'error': err_msg
            }
            return jsonify(response), 400

        # unload payload
        task_name = payload['name']
        user_name = payload['user']
        priority = payload.get('priority', 0)
        data = payload['data']
        lb_mgmt_ip = data['lb-mgmt-ip']
        module = data['module']
        daemons = data.get('daemons', '')
        mode = data['mode']

        # persist to db
        user = User.get_user_by_name(name=user_name)
        if not user:
            email = payload.get('email', '%s@company.com' % user_name)
            user = User(name=user_name, email=email)
        user.last_login = datetime.now()

        task = CodeCoverageTask(
            status=TaskStatus.RECEIVED,
            type='code_coverage_task',
            name=task_name,
            user=user,
            priority=priority,
            lb_mgmt_ip=lb_mgmt_ip,
            module=module,
            daemons=daemons,
            mode=mode
        )
        db.session.add(task)
        try_commit(db.session)

        task.selflink = 'http://localhost' + url_for('task_info', task_id=task.id) # noqa
        db.session.add(task)
        try_commit(db.session)

        db.session.add(
            TaskMsg(task_id=task.id, msg="Received request for task %s." % task) # noqa
        )
        try_commit(db.session)

        # schedule task on worker
        future_result = code_coverage_task.apply_async(
            (task.id, lb_mgmt_ip, module, daemons, mode),
            queue='code-coverage'
        )

        # persist to db
        result = Result(
            id=future_result.id,
            selflink = 'http://localhost' + url_for('task_result', future_result_id=future_result.id) # noqa
        )
        db.session.add(result)
        try_commit(db.session)

        task.status = TaskStatus.SCHEDULED
        task.future_result_id = future_result.id
        db.session.add(task)
        try_commit(db.session)

        db.session.add(
            TaskMsg(task_id=task.id, msg="Scheduled task %s." % task)
        )
        try_commit(db.session)

        response = {
            'selflink': task.selflink,
            'resultlink': result.selflink
        }
        return (jsonify(response),
               202,
               {'Location': url_for('task_result', future_result_id=future_result.id)}) # noqa


@app.route(URI_API+'/task/code-coverage/<task_id>', methods=['GET'])
def task_code_coverage_info(task_id):
    task = Task.query.filter_by(id=task_id).first()
    response = task.to_dict()
    response.update({
        'messages': [repr(task_msg) for task_msg in TaskMsg.get_msgs_by_task_id(task_id)] # noqa
    })
    return jsonify(response)
