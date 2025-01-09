# users.py

from datetime import datetime 
from flask import abort, make_response
import pyodbc
import requests

from config import db
from models import TUser, tuser_schema, tusers_schema
auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'

def read_all(Email,PassWord):
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
                users = TUser.query.all()
                return tusers_schema.dump(users)
            else:
                print (" Log in failed")
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print("Response is not valid JSON. Raw response content:")
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")
        print("Response content:", response.text)
   

def read_one(UserID,Email,PassWord):
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
                user = TUser.query.filter(TUser.UserID == UserID).one_or_none()
                if user is not None:
                    return tuser_schema.dump(user)
                else:
                    abort(
                        404, f"User with ID {UserID} not found"
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
    

def update(UserID,Email,PassWord, tuser): 
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            if json_response[1] == 'True':
                existing_user = TUser.query.get(UserID)
                if existing_user:
                    update_tuser = tuser_schema.load(tuser, session=db.session)
                    existing_user.Email_address = update_tuser.Email_address
                    existing_user.Role = update_tuser.Role
                    existing_user.User_Name = update_tuser.User_Name
                    existing_user.PassWord = update_tuser.PassWord
                    db.session.merge(existing_user)
                    db.session.commit()
                    return tuser_schema.dump(existing_user), 201
                else:
                    abort(404, f"User with ID {UserID} not found")
            else:
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")

def delete(UserID,Email,PassWord):
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
                existing_user = TUser.query.get(UserID)
                if existing_user:
                    db.session.delete(existing_user)
                    db.session.commit()
                    return make_response(f"{UserID} successfully deleted",204)
                else:
                    abort(404, f"User with ID {User_id} not found")
            else:
                print (" Log in failed")
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print("Response is not valid JSON. Raw response content:")
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")
        print("Response content:", response.text)
    

def create(Email,PassWord,user):
    credentials = {
        'email' : Email, 
        'password' : PassWord
    }
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        try:
            json_response = response.json()
            if json_response[1] == 'True':
                UserID = user.get("UserID")
                existing_user = TUser.query.filter(TUser.UserID == UserID).one_or_none()
                if existing_user is None:
                    new_user = tuser_schema.load(user, session=db.session)
                    db.session.add(new_user)
                    db.session.commit()
                    return tuser_schema.dump(new_user), 201
                else:
                    abort(406, f"user with ID {UserID} already exists")
    
            else:
                abort(406, f"Could not authenticate")
                
        except requests.JSONDecodeError:
            print(response.text)
    else:
        print(f"Authentication failed with status code {response.status_code} ")