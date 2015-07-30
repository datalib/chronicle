from flask import Flask, redirect
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return redirect('/static/index.html')


from chronicle.models import Event

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(
    Event,
    # Exposes the Event models at /api/event
    url_prefix='/api',
    collection_name='event',
    methods=['GET'],
    # by default the dates are flattened, we
    # want to have nested dates.
    exclude_columns=['year', 'month', 'day'],
    include_methods=['date'],
)
