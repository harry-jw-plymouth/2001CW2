# trail_features.py

from flask import make_response, abort
import requests

from config import db
from models import Trail_Feature, trailfeature_schema, trailfeatures_schema
auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'


def read_all():
    trailfeatures = Trail_Feature.query.all()
    return trailfeatures_schema.dump(trailfeatures)

def read_one_trails_features(TrailID):
    trailfeatures = Trail_Feature.query.filter(Trail_Feature.TrailID == TrailID).all()
    return trailfeatures_schema.dump(trailfeatures)

def create(Email,PassWord,trailfeature): 
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            if json_response[1] == 'True':
                ID = trailfeature.get("Feature_ID")
                TrailID = trailfeature.get("TrailID")
                existing_trailfeature = Trail_Feature.query.filter(Trail_Feature.Feature_ID == ID).filter(Trail_Feature.TrailID == TrailID).one_or_none()
                if existing_trailfeature is None:
                    new_trailfeature = trailfeature_schema.load(trailfeature, session=db.session)
                    db.session.add(new_trailfeature)
                    db.session.commit()
                    return trailfeature_schema.dump(new_trailfeature), 201
                else:
                    abort(406, f"trail Feature with IDs {ID},{TrailID} already exists")
            else:
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")


def delete(FeatureID,TrailID,Email,PassWord):
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            if json_response[1] == 'True':
                existing_trailfeature = Trail_Feature.query.filter(Trail_Feature.Feature_ID == FeatureID , Trail_Feature.TrailID == TrailID).one_or_none()
                if existing_trailfeature:
                    db.session.delete(existing_trailfeature)
                    db.session.commit()
                    return make_response(f"{FeatureID},{TrailID} successfully deleted", 200)
                else:
                    abort(
                        404, f" trail Feature with id {FeatureID},{TrailID} not found"
                    ) 
            else:
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")