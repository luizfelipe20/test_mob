import os
from flask import Flask
from flask_cors import CORS
from .extensions import mongo
from .main import main

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
    mongo.init_app(app)
    CORS(app)
    app.register_blueprint(main)

    return app