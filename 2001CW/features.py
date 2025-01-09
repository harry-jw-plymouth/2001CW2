# features.py

from flask import make_response, abort

from config import db
from models import Feature, feature_schema, features_schema
import requests
auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'


def read_all():
    features = Feature.query.all()
    return features_schema.dump(features)

def read_one(FeatureID):
    feature = Feature.query.filter(Feature.Feature_ID == FeatureID).one_or_none()
    if feature is not None:
        return feature_schema.dump(feature)
    else:
        abort(404, f"Feature with ID {FeatureID} not found")

def create(Email,PassWord,feature):
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            if json_response[1] == 'True':
                ID = feature.get("Feature_ID")
                existing_feature = Feature.query.filter(Feature.Feature_ID == ID).one_or_none()
                if existing_feature is None:
                    new_feature = feature_schema.load(feature, session=db.session)
                    db.session.add(new_feature)
                    db.session.commit()
                    return feature_schema.dump(new_feature), 201
                else:
                    abort(406, f"Feature with ID {ID} already exists")
            else:
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")

def update(FeatureID,Email,PassWord, feature):
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            if json_response[1] == 'True':
                existing_feature = Feature.query.filter(Feature.Feature_ID == FeatureID).one_or_none()
                if existing_feature:
                    update_feature = feature_schema.load(feature, session=db.session)
                    existing_feature.Name = update_feature.Name
                    db.session.merge(existing_feature)
                    db.session.commit()
                    return feature_schema.dump(existing_feature), 201
                else:
                    abort(404, f"Feature with ID {FeatureID} not found")
            else:
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")



def delete(FeatureID,Email,PassWord):
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            if json_response[1] == 'True':
                existing_feature = Feature.query.filter(Feature.Feature_ID == FeatureID).one_or_none()
                if existing_feature:
                    db.session.delete(existing_feature)
                    db.session.commit()
                    return make_response(f"{FeatureID} successfully deleted", 200)
                else:
                    abort(
                        404, f"Feature with id {FeatureID} not found"
        )
            else:
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")