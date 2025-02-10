from flask import Flask
from .routes import configure_routes

def create_app(config_object='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    configure_routes(app)
    
    return app
