# users.py

from datetime import datetime 
from flask import abort, make_response
import pyodbc

from config import db
from models import TUser, tuser_schema, tusers_schema

def read_one(UserID):
    print(UserID)
    user = TUser.query.get(UserID)
    
    if user is not None:
        return tuser_schema.dump(TUser)
    else:
        abort(
            404, f"User with ID {UserID} not found"
        )

def update(UserID, tuser):
    existing_user = TUser.query.get(UserID)
    if existing_user:
        update_user = tuser_schema.load(tuser)
        existing_user.conten = update_tuser.content
        db.session.merge(existing_user)
        db.session.commit()
        return tuser_schema.dump(existing_user), 201
    else:
        abort(404, f"User with ID {UserID} not found")

def delete(UserID):
    existing_user = TUser.query.get(UserID)
    if existing_user:
        db.session.delete(existing_note)
        db.session.commit()
        return make_response(f"{UserID} successfully deleted",204)
    else:
        abort(404, f"User with ID {User_id} not found")

def create(user):
    UserID = user.get("UserID")
    existing_user = TUser.query.filter(TUser.UserID == UserID).one_or_none()
    if existing_user is None:
        new_user = tuser_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return tuser_schema.dump(new_user), 201
    else:
        abort(406, f"user with ID {UserID} already exists")
    