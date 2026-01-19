# SSUET Event Management System

A web-based event management system for Sir Syed University of Engineering & Technology.

## Overview

This is a Flask-based web application that allows students to browse, search, and register for campus events at SSUET. The system features event listings, detailed event pages, registration forms, and contact functionality.

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, Tailwind CSS, JavaScript
- Data Storage: JSON files
- Design: SSUET official colors (Purple #662D91, Green #34B04A)

## Project Structure

```
SSUET-EVENT-MANAGEMENT/
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── images/events/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── events.html
│   ├── event-detail.html
│   ├── about.html
│   ├── contact.html
│   └── 404.html
├── data/
│   └── events.json
├── app.py
└── requirements.txt
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/ssuet-event-management.git
cd ssuet-event-management
```

2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

5. Open browser and navigate to `http://127.0.0.1:5000`

## Features

- Browse all campus events
- Search and filter events by category and level
- View detailed event information
- Event registration system
- Contact form with inquiry types
- Responsive design for mobile and desktop
- Real-time seat availability tracking

## Pages

- Home - Featured events and statistics
- Events - Complete event listing with filters
- Event Detail - Full event information and registration
- About - University mission and values
- Contact - Contact form and information

## Configuration

Edit `data/events.json` to add or modify events:

```json
{
  "id": 1,
  "title": "Event Title",
  "category": "Technical",
  "date": "2024-02-10",
  "time": "2:00 PM - 5:00 PM",
  "venue": "Room 301",
  "description": "Event description",
  "image": "event.jpg",
  "organizer": "Department Name",
  "seats_available": 30,
  "total_seats": 50,
  "speaker": "Speaker Name",
  "level": "Beginner",
  "duration": "3 hours"
}
```

## Requirements

- Python 3.11+
- Flask 2.3.0
- Modern web browser

## Future Improvements

- Database integration (PostgreSQL/MongoDB)
- User authentication system
- Email notifications
- Admin panel for event management
- QR code ticket generation
- Payment integration
- Analytics dashboard

## Contact

SSUET Event Management Team
events@ssuet.edu.pk
Sir Syed University of Engineering & Technology

## License

This project is developed for educational purposes as part of university coursework.