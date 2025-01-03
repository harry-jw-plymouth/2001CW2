# trail_features.py

from flask import make_response, abort

from config import db
from models import Trail_Feature, trailfeature_schema, trailfeatures_schema


def read_all():
    trailfeatures = Trail_Feature.query.all()
    return trailfeature_schema.dump(trailfeatures)

def read_one_trails_features(TrailID):
    trailfeatures = Trail_Feature.query.all().filter(Trail_Feature.TrailID == TrailID).one_or_none()
    return trailfeature_schema.dump(trailfeatures)

def create(trailfeature):
    ID = trailfeature.get("Feature_ID")
    TrailID = trailfeature.get("TrailID")
    existing_trailfeature = Trail_Feature.query.filter(Trail_Feature.Feature_ID == ID).filter(Trail_Feature.Trail_ID == TrailID).one_or_none()
    if existing_trailfeature is None:
        new_trailfeature = trailfeature_schema.load(Trail_Feature, session=db.session)
        db.session.add(new_trailfeature)
        db.session.commit()
        return trailfeature_schema.dump(new_trailfeature), 201
    else:
        abort(406, f"trail Feature with IDs {ID},{TrailID} already exists")


def delete(FeatureID,TrailID):
    existing_trailfeature = Trail_Feature.query.filter(Trail_Feature.Feature_ID == FeatureID , Trail_Feature.TrailID == TrailID).one_or_none()
    
    if exisiting_trailfeature:
        db.session.delete(existing_trailfeature)
        db.session.commit()
        return make_response(f"{FeatureID},{TrailID} successfully deleted", 200)
    else:
        abort(
            404, f" trail Feature with id {FeatureID},{TrailID} not found"
        )