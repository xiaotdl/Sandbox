from flask import jsonify
from flask import render_template
from flask import flash
from flask import current_app
from flask import abort

from middleware import candidate_by_id
from middleware import candidate
from middleware import add_candidate
from middleware import update_candidate
from middleware import random_candidates
from middleware import delete_candidate
from middleware import random_projects
from middleware import add_project
from middleware import initialize_database as init_db
from middleware import fill_database as fill_db
from middleware import build_message

from decorators import authenticate

def init_api_routes(app):
    if app:
        app.add_url_rule('/api/candidates/<string:id>', 'candidate_by_id', candidate_by_id, methods=['GET'])
        app.add_url_rule('/api/candidates', 'candidate', candidate, methods=['GET'])
        app.add_url_rule('/api/candidates', 'add_candidate', add_candidate, methods=['POST'])
        app.add_url_rule('/api/candidates/<string:id>', 'update_candidate', update_candidate, methods=['PUT'])
        app.add_url_rule('/api/candidates/random', 'get_one_random_candidate', random_candidates,
                         methods=['GET'], defaults={'nr_of_items': 1})
        app.add_url_rule('/api/candidates/random/<int:nr_of_items>', 'get_random_candidates', random_candidates,
                         methods=['GET'])
        app.add_url_rule('/api/candidates/<string:id>', 'delete_candidate', delete_candidate, methods=['DELETE'])
        app.add_url_rule('/api/project/random/<int:nr_of_items>', 'get_random_projects', random_projects,
                         methods=['GET'])
        app.add_url_rule('/api/project', 'add_project', add_project, methods=['POST'])
        app.add_url_rule('/api/initdb', 'initdb', initialize_database)
        app.add_url_rule('/api/filldb', 'filldb', fill_database)
        app.add_url_rule('/api', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})

@authenticate
def page_about():
    if current_app:
        flash('The application was loaded', 'info')
        flash('The secret key is {0}'.format(current_app.config['SECRET_KEY']), 'info')

    return render_template('about.html', selected_menu_item="about")


def page_project():
    return render_template('project.html', selected_menu_item="project")


def page_experience():
    return render_template('experience.html', selected_menu_item="experience")


def page_candidate():
    current_candidates = candidate(serialize=False)
    return render_template('candidate.html', selected_menu_item="candidate", candidates=current_candidates)


def page_add_candidate():
    return render_template('add_candidate.html', selected_menu_item="candidate")


def page_index():
    return render_template('index.html', selected_menu_item="index")


def crash_server():
    abort(500)


def initialize_database():
    message_key = "Initialize Database"
    try:
        init_db()
    except ValueError as err:
        return jsonify(build_message(message_key, err.message))

    return jsonify(build_message(message_key, "OK"))


def fill_database():
    message_key = "Fill Database"
    try:
        fill_db()
    except ValueError as err:
        return jsonify(build_message(message_key, err.message))

    return jsonify(build_message(message_key, "OK"))


def init_website_routes(app):
    if app:
        app.add_url_rule('/crash', 'crash_server', crash_server, methods=['GET'])
        app.add_url_rule('/about', 'page_about', page_about, methods=['GET'])
        app.add_url_rule('/project', 'page_project', page_project, methods=['GET'])
        app.add_url_rule('/candidate', 'page_candidate', page_candidate, methods=['GET'])
        app.add_url_rule('/candidate/add', 'page_add_candidate', page_add_candidate, methods=['GET'])
        app.add_url_rule('/experience', 'page_experience', page_experience, methods=['GET'])
        app.add_url_rule('/', 'page_index', page_index, methods=['GET'])


def handle_error_404(error):
    flash('Server says: {0}'.format(error), 'error')
    return render_template('404.html', selected_menu_item=None)


def handle_error_500(error):
    flash('Server says: {0}'.format(error), 'error')
    return render_template('500.html', selected_menu_item=None)


def init_error_handlers(app):
    if app:
        app.error_handler_spec[None][404] = handle_error_404
        app.error_handler_spec[None][500] = handle_error_500


def list_routes(app):
    result = []
    for rt in app.url_map.iter_rules():
        result.append({
            'methods': list(rt.methods),
            'route': str(rt)
        })
    return jsonify({'routes': result, 'total': len(result)})
