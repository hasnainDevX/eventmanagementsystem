from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Function to get events from a JSON file
def getEvents():
    filePath = "data/events.json"
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            return json.load(f)
    else:
        with open(filePath, "w") as f:
            json.dump([], f)
        return []

# Function to get a single event by its ID
def getEventById(eventId):
    events = getEvents()
    for event in events:
        if event[id] == eventId:
            return event
    return None

# ROUTES 
# Home page route 
@app.route('/')
def index():
    events = getEvents()  # Get all events
    featuresEvents = events[:3] # Slice the first 3 events to show in featured section
    return render_template("index.html", featuresEvents=featuresEvents)

# Events page route
@app.route('/events')
def events():
    allEvents = getEvents()
    return render_template("events.html", events = allEvents)

# event detail page route
@app.route('/events/<int:event_id>')
def event(eventId):
    event = getEventById(eventId)
    if event:
        return render_template("event-detail.html", event = event)
    else:
        return render_template("404.html"), 404
    
# Event registration page route
@app.route("/register/<int:eventId>")
def register(eventId):
    event = getEventById(eventId)
    if event:
        return render_template("register.html", event=event)
    else:
        return render_template("404.html"), 404

# dashboard page route
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# about page route
@app.route('/about')
def about():
    return render_template("about.html")

# contact page route
@app.route('/contact')
def contact():
    return render_template("contact.html")

# 404 error handler
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
