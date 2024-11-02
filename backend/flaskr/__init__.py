import os

from flask import Flask, jsonify, render_template, request
#from backend.School import Event

attendees = 0

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
        response = {
            'message': 'Hello, this is a JSON response!'
        }
        return jsonify(response)

    @app.route("/addevent")
    def create_event():
        response = {
            'message': 'Hello, this is a JSON response!'
        }
        return jsonify(response)

    @app.route("/submit", methods=["POST"])
    def submit_event():
        name = request.form.get("eventName")
        location = request.form.get("eventLocation")
        school_class = request.form.get("eventClass")
        professor = request.form.get("eventProfessor")
        major = request.form.get("Major")
        hours = request.form.get("Hours")

        #event = Event(name, location, school_class, professor, major, hours)

    @app.route("/attend")
    def attend():
        global attendees
        attendees += 1
        return str(attendees)
    
    @app.route("/goback")
    def goback():
        return render_template("index.html")

    return app