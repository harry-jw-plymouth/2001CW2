# features.py

from flask import make_response, abort

from config import db
from models import Feature, feature_schema, features_schema


def read_all():
    features = Feature.query.all()
    return feature_schema.dump(features)

def read_one(FeatureID):
    feature = Feature.query.filter(Feature.Feature_ID == FeatureID).one_or_none()
    if feature is not None:
        return feature_schema.dump(feature)
    else:
        abort(404, f"Feature with ID {FeatureID} not found")

def create(feature):
    ID = feature.get("Feature_ID")
    existing_feature = Feature.query.filter(Feature.Feature_ID == ID).one_or_none()
    if existing_feature is None:
        new_feature = feature_schema.load(Feature, session=db.session)
        db.session.add(new_feature)
        db.session.commit()
        return feature_schema.dump(new_feature), 201
    else:
        abort(406, f"Feature with ID {ID} already exists")

def update(FeatureID, feature):
    existing_feature = Feature.query.filter(Feature.Feature_ID == FeatureID).one_or_none()
    if existing_feature:
        update_feature = feature_schema.load(feature, session=db.session)
        existing_feature.Feature_ID = update_feature.Feature_ID
        db.session.merge(existing_feature)
        db.session.commit()
        return feature_schema.dump(existing_feature), 201
    else:
        abort(404, f"Feature with ID {FeatureID} not found")

def delete(FeatureID):
    existing_feature = Feature.query.filter(Feature.Feature_ID == FeatureID).one_or_none()
    
    if exisiting_feature:
        db.session.delete(existing_feature)
        db.session.commit()
        return make_response(f"{FeatureID} successfully deleted", 200)
    else:
        abort(
            404, f"Feature with id {FeatureID} not found"
        )