import os

from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests
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
                    row_split = str(row).split(',')
                    events.append(row_split)
        print(events, 'events')
        return render_template("index.html", events=events)

    @app.route("/submit", methods=["POST"])
    def submit_event():
        name = request.form.get("eventName")
        location = request.form.get("eventLocation")
        school_class = request.form.get("eventClass")
        professor = request.form.get("eventProfessor")
        major = request.form.get("eventMajor")
        date = request.form.get("eventDate")
        time = request.form.get("eventTime")

        CSV_file = Path('events.csv')
        event = Event(str(uuid.uuid4()), name, location, school_class, professor, major, time, date)
        with CSV_file.open(mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(event.event_list())
        return redirect(url_for('home'))
    
    @app.route("/addEvent")
    def addEvent():
        return render_template("addEvent.html")
    
    @app.route("/attend", methods=["POST"])
    def attend():
        event_id = request.form.get("event_id")
        event_id = event_id.replace("[","").replace("'","")
        CSV_file = Path('events.csv')
        events = []
        with CSV_file.open(mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                events.append(row)
        print(events)
        for row in events:
            print(row[0])
            print(event_id)
            if row[0] == event_id:
                print(row[0], row[8])
                row[8] = str(int(row[8]) + 1)
                break
        with CSV_file.open(mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(events)
        return redirect(url_for('home'))

    @app.route("/goback")
    def goback():
        return render_template("index.html")

    @app.route("/filter", methods=["POST"])
    def filter_events():
        search_query = request.form.get("className")
        
        if not search_query:
            return jsonify({"error": "Class name is required"}), 400

        events = []
        CSV_file = Path('events.csv')
        if CSV_file.exists():
            with CSV_file.open(mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    event = Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])  # Adjust indices based on CSV structure
                    events.append(event)

        filtered_events = [event.event_list() for event in events if search_query.lower() in event.school_class.lower()]

        return jsonify(filtered_events)

    @app.route("/getRec", methods=["POST"])
    def recommendation():
        location = request.form.get("recLocation")
        
        if not location:
            return jsonify({"error": "Location is required"}), 400

        url = "https://api.yelp.com/v3/businesses/natural_language_search"
        payload = {
            "messages": [{"content": "study spots and cafes"}],
            "location": "Irvine",
            "timezone": "America/New_York"
        }

        header = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": "Bearer 6jsrkDuonkZm550GADNb_xr3zEfpQzbn8cpYbBe6UEznghFZkt-Rfgmjx0Qmuy7K3fuuHrbdC82xNNZZTmiaXHSrpjr94ymQh27vNmwuB_uYVd1VADZmdnu2FrAmZ3Yx"
        }
        
        try:
            response = requests.get(url, params=payload, headers=header)
            response.raise_for_status()
            
            businesses = response.json().get("businesses", [])
            
            
            recommendations = [
                {
                    "name": business.get("name"),
                    "address": ", ".join(business["location"]["display_address"]),
                    "image_url": business.get("photos")
                }
                for business in businesses
            ]
            print(recommendations)
            
            return jsonify(recommendations)
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500
    
    return app
