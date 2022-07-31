import os
from flask import Flask,jsonify
from flask_mysqldb import MySQL


def create_app(test_config=None):
    #configure/create app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MYSQL_HOST='localhost',
        MYSQL_USER='root',
        MYSQL_PASSWORD='password1',
        MYSQL_DB='quicklapse'
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
        return "hello, world! may I take your order?"
    return app