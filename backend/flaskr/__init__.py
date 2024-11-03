import os

from flask import Flask, jsonify, render_template, request
from flaskr.School import Event
import uuid
from pathlib import Path
import csv
import os
import requests
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
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
                    # Assuming the row contains values in the order as defined in Event
                    event = Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])  # Adjust indices based on CSV structure
                    events.append(event)

        # Filter events based on the school_class attribute
        filtered_events = [event.event_list() for event in events if search_query.lower() in event.school_class.lower()]

        return jsonify(filtered_events)


    # Define the endpoint to search for study spots
    @app.route("/getRec", methods=["POST"])
    def recommendation():
        # Get the location value from the input JSON data
        location = request.form.get("recLocation")
        
        # Validate that the location was provided
        if not location:
            return jsonify({"error": "Location is required"}), 400
        
        # Yelp API URL and payload
        url = "https://api.yelp.com/v3/businesses/natural_language_search"
        payload = {
            "messages": [{"content": "study spots and cafes"}],
            "location": location,
            "timezone": "America/New_York"
        }

        # Authorization header with API key
        header = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": "Bearer " + "6jsrkDuonkZm550GADNb_xr3zEfpQzbn8cpYbBe6UEznghFZkt-Rfgmjx0Qmuy7K3fuuHrbdC82xNNZZTmiaXHSrpjr94ymQh27vNmwuB_uYVd1VADZmdnu2FrAmZ3Yx"
        }
        

        try:
            response = requests.get(url, params=payload, headers=header)
            response.raise_for_status()
            
            # Parse and filter the JSON response
            businesses = response.json().get("businesses", [])
            
            # Extract only name, address, and image_url for each business
            recommendations = [
                {
                    "name": business.get("name"),
                    "address": ", ".join(business["location"]["display_address"]),
                    "image_url": business.get("photos")
                }
                for business in businesses
            ]
            
            return jsonify(recommendations)
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500
    
    return app


#if __name__ == "__main__":
   # app = create_app()
    #app.run(host='0.0.0.0', port=5000, debug=True)