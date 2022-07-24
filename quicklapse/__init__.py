import os
from flask import Flask


def create_app(test_config=None):
    #configure/create app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'quicklaps.sql')

    )
    if test_config is None: 
        #load instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        os.makedirs(app.instance_path)
    #ensure instance config exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route('/')
    def hello():
        return 'Hello, World! May I take your order?'
    return app