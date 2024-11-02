import os
from flask import Flask, jsonify, render_template, request
#from School import Event, Student


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/addevent")
    def create_event():
        return render_template("insert the html page with add event")

    @app.route("/submit", methods=["POST"])
    def submit_event():
        name = request.form.get("eventName")
        location = request.form.get("eventLocation")
        school_class = request.form.get("eventClass")
        professor = request.form.get("eventProfessor")
        major = request.form.get("Major")
        hours = request.form.get("Hours")


    return app
