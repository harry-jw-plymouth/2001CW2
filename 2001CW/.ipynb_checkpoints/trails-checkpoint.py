# trails.py

from datetime import datetime 
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

TRAILS = {
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
    return list(TRAILS.values())

def create(trail):
    TrailID = trail.get("TrailID")
    Trail_name = trail.get("Trail_name")
    Trail_summary = trail.get("Trail_Summary")
    Trail_Description = trail.get("Trail_Description")
    Difficulty = trail.get("Difficulty")
    Location = trail.get("Location")
    Length = trail.get("Length")
    Elevation_gain = trail.get("Elevation_gain")
    Route_type = trail.get("Route_type")
    OwnerID = trail.get("OwnerID")
    if  TrailID and TrailID not in TRAILS:
        TRAILS[TrailID] = {
            "TrailID": TrailID,
            "Trail_name": Trail_name,
            "Trail_Summary": Trail_summary,
            "Trail_Description": Trail_Description,
            "Difficulty": Difficulty, 
            "Location": Location,
            "Length" : Length,
            "Elevation_gain": Elevation_gain,
            "Route_type": Route_type,
            "OwnerID": OwnerID,
            "timestamp": get_timestamp(),
        }
        return TRAILS[TrailID], 201
    else:
        abort(
            406,
            f"Trail with id {TrailID} already exists",
        )

def read_one(TrailID):
    if TrailID in TRAILS:
        return TRAILS[TrailID]
    else:
        abort(
            404, f"Trail with id {TrailID} not found"
        )

def update(TrailID, Trail):
    if TrailID in TRAILS:
        TRAILS[TrailID]["Trail_name"] = Trail.get("Trail_name", TRAILS[TrailID]["Trail_name"])
        TRAILS[TrailID]["Trail_Summary"] = Trail.get("Trail_Summary", TRAILS[TrailID]["Trail_Summary"])
        TRAILS[TrailID]["Trail_Description"] = Trail.get("Trail_Description", TRAILS[TrailID]["Trail_Description"])
        TRAILS[TrailID]["Difficulty"] = Trail.get("Difficulty", TRAILS[TrailID]["Difficulty"])
        TRAILS[TrailID]["Location"] = Trail.get("Location", TRAILS[TrailID]["Location"])
        TRAILS[TrailID]["Length"] = Trail.get("Length", TRAILS[TrailID]["Length"])
        TRAILS[TrailID]["Elevation_gain"] = Trail.get("Elevation_gain", TRAILS[TrailID]["Elevation_gain"])
        TRAILS[TrailID]["Route_type"] = Trail.get("Route_type", TRAILS[TrailID]["Route_type"])
        TRAILS[TrailID]["OwnerID"] = Trail.get("OwnerID", TRAILS[TrailID]["OwnerID"])
        TRAILS[TrailID]["timestamp"] = get_timestamp()
        return TRAILS[TrailID]
    else:
        abort(
            404, f"Trail with ID {TrailID} not found"
        )

def delete(TrailID):
    if TrailID in TRAILS:
        del TRAILS[TrailID]
        return make_response(
            f"{TrailID} Successfully deleted", 200
        )
    else:
        abort(
            404, f"Trail with id {TrailID} not found"
        )