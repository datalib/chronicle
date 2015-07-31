from time import time
from email.utils import formatdate

from flask import Flask, redirect
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///history.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return redirect('/static/index.html')


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 's-maxage=86400, max-age=86400'
    response.headers['Expires'] = formatdate(time() + 86400)
    return response


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
    # Usually one would want to get >10
    # results per page
    results_per_page=30,
)
