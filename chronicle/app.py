from flask import Flask, abort, request
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
db = SQLAlchemy(app)


from chronicle.models import Event

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(
    Event,
    # Exposes the Event models at /api instead
    # of the default /api/event
    url_prefix='/api',
    collection_name='',
    methods=['GET'],
    # by default the dates are flattened, we
    # want to have nested dates.
    exclude_columns=['year', 'month', 'day'],
    include_methods=['date'],
)
