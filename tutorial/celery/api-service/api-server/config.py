import os
import sys


class Config(object):
    # == app server ==
    PUBLIC_IP = '10.192.10.198'
    HOST = '0.0.0.0'
    # PORT = 5000 # used during testing
    PORT = 80

    # Flask and some of its extensions use this secret key as a cryptographic
    # key to generate signatures or tokens.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # == db ==
    SQLALCHEMY_DATABASE_URI = \
        'mysql+mysqldb://root:default@localhost:3306/api_svr_db'
    # Disable signaling to application every time a change is about to be made
    # in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # == celery ==
    WORKER_MODULE_PATH = os.path.abspath('../worker')
    if os.path.dirname(WORKER_MODULE_PATH) not in sys.path:
        sys.path.append(os.path.dirname(WORKER_MODULE_PATH))
