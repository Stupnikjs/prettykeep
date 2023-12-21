from flask import Flask



def create_app(blueprint:str):

    app = Flask(__name__, template_folder="static/templates")

    app.register_blueprint(blueprint=blueprint)
    
    return app