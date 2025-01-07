# locationpt.py

from datetime import datetime 
from flask import abort, make_response
import pyodbc

from config import db, ma
from models import Location_Pt, location_pt_schema, location_pts_schema

def read_all():
    pts = Location_Pt.query.all()        
    return location_pts_schema.dump(pts)
    #return list(TRAILS2.values())


def create(locationpt):
    Location_Point = locationpt.get("Location_Point")
    existing_pt = Location_Pt.query.filter(Location_Pt.Location_Point == Location_Point).one_or_none()
    if existing_pt is None:
        new_pt = location_pt_schema.load(locationpt, session=db.session)
        db.session.add(new_pt)
        db.session.commit()
        return location_pt_schema.dump(new_pt), 201
    else:
        abort(406, f"point with ID {Location_Point} already exists")

def read_one(LocationPoint):
    pt = Location_Pt.query.filter(Location_Pt.Location_Point == LocationPoint).one_or_none()
    if pt is not None:
        return location_pt_schema.dump(pt)
    else:
        abort(404, f"point with id {LocationPoint} not found")

def update(LocationPoint, point):
    existing_pt = Location_Pt.query.filter(Location_Pt.Location_Point == LocationPoint).one_or_none() 
    if existing_pt:
        update_pt = location_pt_schema.load(point, session=db.session)
        existing_pt.Latitude = update_pt.Latitude
        existing_pt.Longitude = update_pt.Longitude
        existing_pt.Description = update_pt.Description
        db.session.merge(existing_pt), 201
        db.session.commit()
        return location_pt_schema.dump(existing_pt)
    else:
        abort(
            404, f"Point with ID {LocationPoint} not found"
        )

def delete(LocationPoint):
    existing_pt = Location_Pt.query.filter(Location_Pt.Location_Point == LocationPoint).one_or_none()
    
    if existing_pt:
        db.session.delete(existing_pt)
        db.session.commit()
        return make_response(f"{LocationPoint} successfully deleted", 200)
    else:
        abort(
            404, f"point with id {LocationPoint} not found"
        )