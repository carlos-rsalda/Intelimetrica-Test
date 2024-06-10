from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api # type: ignore
from flasgger import Swagger # type: ignore

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    api = Api(app)
    swagger = Swagger(app)

    from app.resources import RestaurantResource, RestaurantListResource, RestaurantStatisticsResource
    api.add_resource(RestaurantListResource, '/restaurants')
    api.add_resource(RestaurantResource, '/restaurants/<string:id>')
    api.add_resource(RestaurantStatisticsResource, '/restaurants/statistics')

    return app
