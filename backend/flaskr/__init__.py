import os

from flask import Flask, jsonify, render_template, request
from flaskr.School import Event
import uuid
from pathlib import Path
import csv

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
        events = []
        CSV_file = Path('events.csv')
        if CSV_file.exists():
            with CSV_file.open(mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    events.append(row)
        return render_template("addEvent.html", events=events)

    @app.route("/submit", methods=["POST"])
    def submit_event():
        name = request.form.get("eventName")
        location = request.form.get("eventLocation")
        school_class = request.form.get("eventClass")
        professor = request.form.get("eventProfessor")
        major = request.form.get("Major")
        date = request.form.get("eventDate")
        time = request.form.get("eventTime")

        CSV_file = Path('events.csv')
        event = Event(str(uuid.uuid4()), name, location, school_class, professor, major, time, date)
        with CSV_file.open(mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(event.event_list())
        return render_template("index.html")

    # @app.route("/attend", methods=["POST"])
    # def attend(event_id):
    #     event = events[event_id - 1]
    #     event.add_attendee()
    #     return event.attendees
    
    @app.route("/goback")
    def goback():
        return render_template("index.html")
    
    # @app.route("/search")
    # def search():
    #     query = request.form.get("search")
    #     results = [event for event in events if any(query in getattr(event, attr).lower() for attr in ['name', 'location', 'school_class', 'professor', 'major', 'time', 'date'])]
    #     return results



# goback event
# attend event
