from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    swagger = Swagger(app)

    with app.app_context():
        from . import routes 
        app.register_blueprint(routes.main)
        db.create_all()

    return app
