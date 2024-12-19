# models.py

from datetime import datetime
from marshmallow_sqlalchemy import fields
from sqlalchemy import inspect
import pytz

from config import db, ma

class Trail_Feature(db.Model):
    __tablename__ = "Trail_FeatureTest"
    TrailID = db.Column(db.Integer, primary_key=True)
    Trail_FeatureID = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )
class Trail_FeatureSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Trail_Feature
        load_instance = True
        sqla_session = db.session
        include_fk = True

class Trail(db.Model):
    __tablename__ = "TrailTest"
    TrailId=db.Column(db.Integer, primary_key=True)
    Trail_name=db.Column(db.String(60), unique=True)
    Trail_Summary=db.Column(db.String(6000))
    Trail_Description=db.Column(db.String(6000))
    Difficulty=db.Column(db.String(10))
    Length=db.Column(db.Float)
    Elevation_gain=db.Column(db.Float)
    Route_type=db.Column(db.String(10))
    OwnerID=db.Column(db.Integer)
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )
   # trail_features = db.relationship(
    #    Trail_Feature,
     #   backref="trail",
      #  cascade="all, delete, delete-orphan",
       # single_parent=True,
        #order_by="desc(Trail_Feature.timestamp)"
    #)
    

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session
        include_relationships = True
    trail_features = fields.Nested(Trail_FeatureSchema, many=True)

trail_feature_schema = Trail_FeatureSchema()
trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
    

