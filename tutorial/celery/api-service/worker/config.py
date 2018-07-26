class Config(object):
    # == worker ==
    WORKER_MGMT_IP = '10.192.10.233'
    WORKER_WEB_SERVER_ROOT_FOLDER = '/var/www/html'

    # == db ==
    MYSQL_HOST = '10.192.10.198'
    MYSQL_USER = 'worker'
    MYSQL_PASS = 'worker'
    MYSQL_DB = 'api_svr_db'

    # == celery ==
    CELERY_IMPORTS = (
        'worker.app.test.tasks',
        'worker.app.code_coverage.tasks',
        'worker.app.core_extraction.tasks',
        )

    CELERY_ROUTES = ([
        ('worker.app.code_coverage.tasks.*', {'queue': 'test'}),
        ('worker.app.code_coverage.tasks.*', {'queue': 'code-coverage'}),
        ('worker.app.core_extraction.tasks.*', {'queue': 'core-extraction'}),
    ],)

    BROKER_URL = 'amqp://admin:admin@10.192.10.198/'
    CELERY_RESULT_BACKEND = 'redis://10.192.10.198:6379/0'
    CELERY_RESULT_PERSISTENT = True  # message persist after a broker restart
    CELERY_TASK_RESULT_EXPIRES = 0  # never expire
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

    # == code coverage ==
    CODE_COVERAGE_BINDIR = '/root/git/code-coverage'
    CODE_COVERAGE_TMPDIR = '/tmp/service/code-coverage'
    CODE_COVERAGE_OUTDIR = \
        WORKER_WEB_SERVER_ROOT_FOLDER + '/service/code-coverage'
