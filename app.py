from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Data functions
def getEvents():
    filePath = "data/events.json"
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            return json.load(f)
    return []

def getEventById(eventId):
    events = getEvents()
    for event in events:
        if event['id'] == eventId:
            return event
    return None

# Routes
@app.route('/')
def index():
    events = getEvents()
    featuredEvents = events[:3]
    return render_template("index.html", featuredEvents=featuredEvents)

@app.route('/events')
def events():
    allEvents = getEvents()
    return render_template("events.html", events=allEvents)

@app.route('/events/<int:eventId>')
def event(eventId):
    event = getEventById(eventId)
    if event:
        return render_template("event-detail.html", event=event)
    return render_template("404.html"), 404

@app.route('/post-event')
def postEvent():
    return render_template("post-event.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/register')
def register():
    return render_template("register.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug=True)