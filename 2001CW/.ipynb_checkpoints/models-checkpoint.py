# models.py

from datetime import datetime
from marshmallow_sqlalchemy import fields, SQLAlchemyAutoSchema, auto_field
import pytz

from config import db, ma



class Location_Pt(db.Model):
    __tablename__ = "Location_Pt"
    Location_Point = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Latitude =db.Column(db.Float)
    Longitude = db.Column(db.Float)
    Description = db.Column(db.String(200))
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )

class Location_PtSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = Location_Pt
        load_instance = True
        sql_Session = db.session

class Trail_LocationPt(db.Model):
    __tablename__ = "Trail_LocationPt"
    TrailID=db.Column(db.Integer, primary_key=True)
    Location_Point = db.Column(db.Integer, primary_key=True)
    Order_no = db.Column(db.Integer)
 #

class Trail_LocationPtSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail_LocationPt
        load_instance = True
        sql_session = db.session

class Trail_Feature(db.Model):
    __tablename__ = "Trail_Feature"
    TrailID=db.Column(db.Integer, primary_key=True)
    Feature_ID=db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )

class Trail_FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail_Feature
        load_instance = True
        sql_session = db.session


class Feature(db.Model):
    __tablename__ = "Feature"
    Feature_ID=db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String(30))
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )

class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Feature
        load_instance = True
        sql_session = db.session
    

class Trail(db.Model):
    __tablename__ = "Trail"
    TrailID=db.Column(db.Integer, primary_key=True)
    Trail_name=db.Column(db.String(60), unique=True)
    Trail_Summary=db.Column(db.String(6000))
    Trail_Description=db.Column(db.String(6000))
    Difficulty=db.Column(db.String(10))
    Location=db.Column(db.String(100))
    Length=db.Column(db.Float)
    Elevation_gain=db.Column(db.Float)
    Route_type=db.Column(db.String(10))
    OwnerID=db.Column(db.Integer, db.ForeignKey("TUser.UserID"))
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )
    

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sql_session = db.session
        include_fk = True
    
        
class TUser(db.Model):
    __tablename__ = "TUser"
    UserID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email_address=db.Column(db.String(60))
    Role=db.Column(db.String(20))
    User_Name=db.Column(db.String(100))
    PassWord=db.Column(db.String(100))
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )
    trails = db.relationship(
        Trail,
        backref="TUser",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Trail.timestamp)"
    )
           
class TUserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TUser
        load_instance = True
        include_relationships = True


location_pt_schema = Location_PtSchema()
location_pts_schema = Location_PtSchema(many = True)
traillocationpt_schema = Trail_LocationPtSchema()
traillocationpts_schema = Trail_LocationPtSchema(many=True)
trailfeature_schema = Trail_FeatureSchema()
trailfeatures_schema = Trail_FeatureSchema(many=True)
tusers_schema=TUserSchema(many=True)
tuser_schema = TUserSchema()
feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)
trail_schema = TrailSchema()
trails_schema = TrailSchema(many =True)
    

