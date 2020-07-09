import os
from flask import Flask
from flask_cors import CORS
from core.extensions import mongo
from core.main import main

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
    mongo.init_app(app)
    CORS(app)
    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == "__main__":
    app.run()