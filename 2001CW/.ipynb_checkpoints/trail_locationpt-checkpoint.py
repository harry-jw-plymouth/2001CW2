# trail_locationpt.py

from flask import make_response, abort

from config import db
from models import Trail_LocationPt, traillocationpt_schema, traillocationpts_schema


def read_all():
    trailocpoints = Trail_LocationPt.query.all()
    return traillocationpt_schema.dump(trailocpoints)

def read_one_trails_points(TrailID):
    trailpoints = Trail_LocationPt.query.all().filter(Trail_LocationPt.TrailID == TrailID).one_or_none()
    return traillocationpt_schema.dump(trailpoints)

def create(traillocationpoint):
    PointID = traillocationpoint.get("Location_Point")
    TrailID = traillocationpoint.get("TrailID")
    existing_traillocpoint = Trail_LocationPt.query.filter(Trail_LocationPt.Location_Point == ID).filter(Trail_LocationPt.Trail_ID == TrailID).one_or_none()
    if  existing_traillocpoint is None:
        new_traillocpoint = traillocationpt_schema.load(Trail_LocationPt, session=db.session)
        db.session.add(new_traillocpoint)
        db.session.commit()
        return traillocationpt_schema.dump(new_traillocpoint), 201
    else:
        abort(406, f"trail point with IDs {PointID},{TrailID} already exists")


def delete(LocationPoint,TrailID):
    existing_traillocpoint = Trail_LocationPt.query.filter(Trail_LocationPt.Location_Point == LocationPoint , Trail_LocationPt.TrailID == TrailID).one_or_none()
    
    if existing_traillocpoint:
        db.session.delete(existing_traillocpoint)
        db.session.commit()
        return make_response(f"{LocationPoint},{TrailID} successfully deleted", 200)
    else:
        abort(
            404, f" trail point with id {LocationPoint},{TrailID} not found"
        )