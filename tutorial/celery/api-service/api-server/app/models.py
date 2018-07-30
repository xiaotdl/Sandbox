from app import db
from datetime import datetime
import enum

from flask import url_for


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    last_login = db.Column(db.DateTime, default=datetime.now)
    selflink = db.Column(db.String(256))

    tasks = db.relationship('Task', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created-at': self.created_at,
            'last-login': self.last_login,
            'tasks': [task.selflink for task in self.tasks],
            'selflink': self.selflink
        }

    @staticmethod
    def get_user_by_name(name):
        user = User.query.filter_by(name=name).first()
        return user


class TaskStatus(enum.Enum):
    RECEIVED = 1
    SCHEDULED = 2
    STARTED = 3
    COMPLETED = 4


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(128))
    priority = db.Column(db.Integer)
    status = db.Column(db.Enum(TaskStatus))
    future_result_id = db.Column(db.String(128), db.ForeignKey('result.id'))
    timestamp = db.Column(db.DateTime, default=datetime.now)
    type = db.Column(db.String(128))
    selflink = db.Column(db.String(256))

    required_entities = ['name', 'user', 'data']

    __mapper_args__ = {
        'polymorphic_identity': 'task',
        'polymorphic_on': type
    }

    def __repr__(self):
        return '<Task {}>'.format(self.name)

    def to_dict(self):
        resultlink = 'N/A'
        result = Result.get_result_by_id(self.future_result_id)
        if result:
            resultlink = result.selflink
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'priority': self.priority,
            'status': str(self.status)[len("TaskStatus."):],
            'future_result_id': self.future_result_id,
            'created-at': self.timestamp,
            'type': self.type,
            'selflink': self.selflink,
            'resultlink': resultlink
        }

    @classmethod
    def validate(self, payload):
        for entity in Task.required_entities:
            if entity not in payload:
                return (False, "entity '%s' is required." % entity)
        return (True, '')

    @staticmethod
    def get_task_by_future_result_id(future_result_id):
        task = Task.query.filter_by(future_result_id=future_result_id).first()
        return task


class TestTask(Task):
    id = db.Column(db.ForeignKey('task.id'), primary_key=True)
    a = db.Column(db.Integer)
    b = db.Column(db.Integer)

    required_entities = ['a', 'b']

    __mapper_args__ = {
        'polymorphic_identity': 'test_task',
    }

    def __repr__(self):
        return '<TestTask {}>'.format(self.id)

    def to_dict(self):
        d = super(TestTask, self).to_dict()
        d.update({
            'a': self.a,
            'b': self.b,
            'selflink': self.get_selflink()
        })
        return d

    def get_selflink(self):
        return 'http://localhost' + url_for('task_test_info', task_id=self.id)

    @classmethod
    def validate(self, payload):
        ok, err_msg = super(TestTask, self).validate(payload)
        if not ok:
            return (False, err_msg)

        for entity in TestTask.required_entities:
            if entity not in payload.get('data', {}):
                return (False, "entity '%s' is required." % entity)
        return (True, '')


class CodeCoverageTask(Task):
    id = db.Column(db.ForeignKey('task.id'), primary_key=True)
    lb_mgmt_ip = db.Column(db.String(128))
    module = db.Column(db.String(64))
    daemons = db.Column(db.String(128))
    mode = db.Column(db.String(64))

    required_entities = ['lb-mgmt-ip', 'module', 'mode']

    __mapper_args__ = {
        'polymorphic_identity': 'code_coverage_task',
    }

    def __repr__(self):
        return '<CodeCoverageTask {}>'.format(self.id)

    def to_dict(self):
        d = super(CodeCoverageTask, self).to_dict()
        d.update({
            'lb_mgmt_ip': self.lb_mgmt_ip,
            'module': self.module,
            'daemons': self.daemons,
            'mode': self.mode,
            'selflink': self.get_selflink()
        })
        return d

    def get_selflink(self):
        return 'http://localhost' + url_for('task_code_coverage_info', task_id=self.id) # noqa

    @classmethod
    def validate(self, payload):
        ok, err_msg = super(CodeCoverageTask, self).validate(payload)
        if not ok:
            return (False, err_msg)

        for entity in CodeCoverageTask.required_entities:
            if entity not in payload.get('data', {}):
                return (False, "entity '%s' is required." % entity)
        return (True, '')


# class CoreExtractionTask(Task):
#     id = db.Column(db.ForeignKey('task.id'), primary_key=True)
#     custom = db.Column(db.String(128))
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'core_extraction_task',
#     }
#
#     def __repr__(self):
#         return '<CoreExtractionTask {}>'.format(self.id)


class TaskMsg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    msg = db.Column(db.String(1024))
    timestamp = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '[%s] %s' % (self.timestamp, self.msg)

    @staticmethod
    def get_msgs_by_task_id(task_id):
        results = TaskMsg.query.filter_by(task_id=task_id).all()
        return results


class Result(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    selflink = db.Column(db.String(256))

    def __repr__(self):
        return '<Result {}>'.format(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'selflink': self.selflink,
        }

    @staticmethod
    def get_result_by_id(id):
        result = Result.query.filter_by(id=id).first()
        return result
