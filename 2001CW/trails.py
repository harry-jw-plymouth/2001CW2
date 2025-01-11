# trails.py

from datetime import datetime 
from flask import abort, make_response
import pyodbc
import requests

from config import db, ma
from models import TUser, tuser_schema ,Trail, trail_schema, trails_schema

auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'


def read_all():
    trails = Trail.query.all()        
    return trails_schema.dump(trails)

def create(Email,PassWord,trail):
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            if json_response[1] == 'True':
                print("Log in success")
                TrailID = trail.get("TrailID")
                existing_trail = Trail.query.filter(Trail.TrailID == TrailID).one_or_none( )
                if existing_trail is None:
                    new_trail = trail_schema.load(trail, session=db.session)
                    db.session.add(new_trail)
                    db.session.commit()
                    return trail_schema.dump(new_trail), 201
                else:
                    abort(406, f"Trail with ID {TrailID} already exists")
            else:
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print("Response is not valid JSON. Raw response content:")
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")

def read_one(TrailID):
    trail = Trail.query.filter(Trail.TrailID == TrailID).one_or_none()
    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail with id {TrailID} not found")

def update(TrailID,Email,PassWord, trail):
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            print("Authenticated successfully:", json_response)
            print(json_response[1])
            if json_response[1] == 'True':
                print("Log in success")
                existing_trail = Trail.query.filter(Trail.TrailID == TrailID).one_or_none() 
                if existing_trail:
                    update_trail = trail_schema.load(trail, session=db.session)
                    existing_trail.Trail_name = update_trail.Trail_name
                    existing_trail.Trail_Summary = update_trail.Trail_Summary
                    existing_trail.Trail_Description = update_trail.Trail_Description
                    existing_trail.Difficulty = update_trail.Difficulty
                    existing_trail.Location = update_trail.Location
                    existing_trail.Length = update_trail.Length
                    existing_trail.Elevation_gain = update_trail.Elevation_gain
                    existing_trail.Route_type = update_trail.Route_type
                    existing_trail.OwnerID = update_trail.OwnerID
                    db.session.merge(existing_trail)
                    db.session.commit()
                    return trail_schema.dump(existing_trail), 201
                else:
                    abort(
                        404, f"Trail with ID {TrailID} not found"
                    )
            else:
                print (" Log in failed")
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print("Response is not valid JSON. Raw response content:")
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")


def delete(TrailID,Email,PassWord):
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            print("Authenticated successfully:", json_response)
            print(json_response[1])
            if json_response[1] == 'True':
                print("Log in success")
                existing_trail = Trail.query.filter(Trail.TrailID == TrailID).one_or_none()
                if existing_trail:
                    db.session.delete(existing_trail)
                    db.session.commit()
                    return make_response(f"{TrailID} successfully deleted", 200)
                else:
                    abort(
                        404, f"Trail with id {TrailID} not found"
                    )     
            else:
                print (" Log in failed")
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print("Response is not valid JSON. Raw response content:")
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")
        print("Response content:", response.text)
    
    
