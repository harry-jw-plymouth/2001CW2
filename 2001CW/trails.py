# trails.py

#from datetime import datetime 
from flask import abort, make_response

from config import db
from models import Trail, trail_schema, trails_schema


def read_all():
    trails = Trail.query.all()
    return trail_schema.dump(trails)

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