"""
james@yggdrasil:~/PycharmProjects/mapadh$ export FLASK_APP=app.py
james@yggdrasil:~/PycharmProjects/mapadh$ flask run
"""

import configparser
import os
from flask import Flask
from flask import render_template
from flask import jsonify
from .censustrips import fetch_population_along_route, fetch_2021_population_along_route
app = Flask(__name__)

if not os.path.exists('CONFIG.ini'):
    print("Warning - no CONFIG.ini with the Pg connection string found")

# TODO: do config better: https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/#the-application-factory
config = configparser.ConfigParser()
config.read('CONFIG.ini')
# postgresql+psycopg2://username:password@host:port/dbname
PG_CONNECTION_STRING = config['Connections']['mapadh-db']


@app.route('/')
def index():
    return 'Index Page'


@app.route('/censustrips_route/<int:route_id>')
def censustrips_route(route_id):
    """
    http://127.0.0.1:5000/censustrips_route/3
    :param route_id: 1
    :return: rendered html template
    """
    route_stops_d = fetch_population_along_route(route_id, pg_conn_str=PG_CONNECTION_STRING)

    # flask knows to look in the templates folder
    # as we have designated our project as a package
    # by using the __init__.py
    return render_template('route.jinja2', route_stops=route_stops_d)


@app.route('/censustrips_route_json/<int:route_id>')
def censustrips_route_json(route_id):
    """
    http://127.0.0.1:5000/censustrips_route_json/3 Edinburgh -> Kings Cross
    :param route_id: 1
    :return: dict as a json
    """
    route_stops_d = fetch_population_along_route(route_id, pg_conn_str=PG_CONNECTION_STRING)
    return jsonify(route_stops_d)


# TODO: test route to return 2021 data - we will want to use the existing route with a year param
@app.route('/censustrips_route_2021_json/<int:route_id>')
def censustrips_route_2021_json(route_id):
    """
    http://127.0.0.1:5000/censustrips_route_json/3 Edinburgh -> Kings Cross
    :param route_id: 1
    :return: dict as a json
    """
    route_stops_d = fetch_2021_population_along_route(route_id, pg_conn_str=PG_CONNECTION_STRING)
    return jsonify(route_stops_d)





