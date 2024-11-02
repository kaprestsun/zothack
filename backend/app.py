from flask import Flask, jsonify, render_template, request
from School import Event, Student
app = Flask(__name__)

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

  


if __name__ == "__main__":
  app.run()

# routes to use