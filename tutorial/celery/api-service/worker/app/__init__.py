from celery import Celery
from worker.config import Config
from worker.app.db import DB


# init celery
celery = Celery(__name__)

# load celery cfg
celery.config_from_object(Config)

# init db
db = DB(Config.MYSQL_HOST, Config.MYSQL_USER, Config.MYSQL_PASS, Config.MYSQL_DB) # noqa
