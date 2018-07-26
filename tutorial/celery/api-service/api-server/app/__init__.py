from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# init app
app = Flask(__name__)

# load cfg
app.config.from_object(Config)

# init DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# put at the bottom to avoid circular imports
from app import routes, models # noqa
db.create_all()
db.session.commit()
