"""
james@yggdrasil:~/PycharmProjects/mapadh$ export FLASK_APP=app.py
james@yggdrasil:~/PycharmProjects/mapadh$ flask run
"""

from flask import Flask
from flask import render_template
from flask import jsonify
from .censustrips import fetch_population_along_route
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/censustrips_route/<int:route_id>')
def censustrips_route(route_id):
    """
    http://127.0.0.1:5000/censustrips_route/1
    :param route_id: 1
    :return: rendered html template
    """
    route_stops_d = fetch_population_along_route(route_id)

    # flask knows to look in the templates folder
    # as we have designated our project as a package
    # by using the __init__.py
    return render_template('route.jinja2', route_stops=route_stops_d)


@app.route('/censustrips_route_json/<int:route_id>')
def censustrips_route_json(route_id):
    """
    http://127.0.0.1:5000/censustrips_route_json/1 Glasgow -> Edinburgh
    http://127.0.0.1:5000/censustrips_route_json/2 Ayr -> Glasgow
    http://127.0.0.1:5000/censustrips_route_json/3 Edinburgh -> Kings Cross
    :param route_id: 1
    :return: dict as a json
    """
    route_stops_d = fetch_population_along_route(route_id)
    return jsonify(route_stops_d)





