# trails.py

from datetime import datetime 
from flask import abort, make_response
import pyodbc

from config import db, ma
from models import Trail, trail_schema, trails_schema

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

server = 'dist-6-505.uopnet.plymouth.ac.uk'
database = 'COMP2001_HWatton'
username = 'HWatton'
password = 'IfrW391*'
driver = '{ODBC Driver 17 for SQL Server}'


conn = pyodbc.connect( 
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=Yes;'
    'TrustServerCertificate=Yes;'
    'Connection Timeout=30;'
    'Trusted_Connection=No'
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM TrailTest")
ts = cursor.fetchall()
for trail in ts:
        print(trail)
#conn = pyodbc.connect(conn_str)

TRAILS2 = {
    1: {
        "TrailID": 1,
        "Trail_name": "Trail 1",
        "Trail_Summary": "This is summary1",
        "Trail_Description": "This is description 1",
        "Difficulty": "Easy", 
        "Location": "England,England,England",
        "Length" : 34.4,
        "Elevation_gain": 23.4,
        "Route_type": "Loop",
        "OwnerID": 1,
        "timestamp": get_timestamp(),
    },
    2: {
        "TrailID": 2,
        "Trail_name": "Trail 2",
        "Trail_Summary": "This is summary2",
        "Trail_Description": "This is description 2",
        "Difficulty": "Easy", 
        "Location": "England,England,England",
        "Length" : 33.2,
        "Elevation_gain": 3.4,
        "Route_type": "Loop",
        "OwnerID": 2,
        "timestamp": get_timestamp(),
    },
    3: {
        "TrailID": 3,
        "Trail_name": "Trail 3",
        "Trail_Summary": "This is summary3",
        "Trail_Description": "This is description 3",
        "Difficulty": "Easy", 
        "Location": "England,England,England",
        "Length" : 24.3,
        "Elevation_gain": 12.4,
        "Route_type": "Loop",
        "OwnerID": 3,
        "timestamp": get_timestamp(),
    }
}



def read_all():
    trails = Trail.query.all()        
    return trail_schema.dump(trails)
    #return list(TRAILS2.values())


def create(trail):
    TrailID = trail.get("TrailID")
    existing_trail = Trail.query.filter(Trail.TrailID == TrailID).one_or_none()
    if existing_trail is None:
        new_trail = trail_schema.load(trail, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
        abort(406, f"Trail with ID {TrailID} already exists")

def read_one(TrailID):
    trail = Trail.query.filter(Trail.TrailID == TrailID).one_or_none()
    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail with id {TrailID} not found")

def update(TrailID, Trail):
    existing_trail = Trail.query.filter(Trail.TrailID == TrailID).one_or_none() 
    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.TrailID = update_trail.TrailID
        db.session.merge(existing_trail), 201
    else:
        abort(
            404, f"Trail with ID {TrailID} not found"
        )

def delete(TrailID):
    existing_trail = Trail.query.filter(Trail.TrailID == TrailID).one_or_none()
    
    if exisiting_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f"{TrailID} successfully deleted", 200)
    else:
        abort(
            404, f"Trail with id {TrailID} not found"
        )