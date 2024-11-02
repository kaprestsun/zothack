import os

from flask import Flask, jsonify, render_template, request
from backend.flaskr.School import Event

events = []

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
        return render_template("index.html", events=events)

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
        date = request.form.get("eventDate")
        time = request.form.get("eventTime")

        event = Event(len(events) + 1, name, location, school_class, professor, major, time, date)
        events.append(event)
        return render_template("insert the html page with add event")

    @app.route("/attend", methods=["POST"])
    def attend(event_id):
        event = events[event_id - 1]
        event.add_attendee()
        return event.attendees
    
    @app.route("/goback")
    def goback():
        return render_template("index.html")
    
    @app.route("/search")
    def search():
        query = request.form.get("search")
        results = [event for event in events if any(query in getattr(event, attr).lower() for attr in ['name', 'location', 'school_class', 'professor', 'major', 'time', 'date'])]
        return results
    
    return app


# goback event
# attend event