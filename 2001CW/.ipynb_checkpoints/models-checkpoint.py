# models.py

from datetime import datetime
from marshmallow_sqlalchemy import fields
import pytz

from config import db, ma


    

#class Trail_Feature(db.Model):
    #__tablename__ = "CW2.Trail_Feature"
    #TrailID=db.Column(db.Integer, primary_key=True, db.ForeignKey("TrailTest.TrailID"))
    #Feature_ID=db.Column(db.Integer, primary_key=True)
    #timestamp = db.Column(
     #   db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
      #  onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    #)

#class Trail_FeatureSchema(ma.SQLAlchemyAutoSchema):
 #   class Meta:
  #      model = Trail_Feature
   #     load_instance = True
    #    sqla_session = db.session
     #   include_fk = True
    

class Trail(db.Model):
    __tablename__ = "CW2.Trail"
    TrailID=db.Column(db.Integer, primary_key=True)
    Trail_name=db.Column(db.String(60), unique=True)
    Trail_Summary=db.Column(db.String(6000))
    Trail_Description=db.Column(db.String(6000))
    Difficulty=db.Column(db.String(10))
    Location=db.Column(db.String(100))
    Length=db.Column(db.Float)
    Elevation_gain=db.Column(db.Float)
    Route_type=db.Column(db.String(10))
    OwnerID=db.Column(db.Integer, db.ForeignKey("CW2.TUser.UserID"))
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )
#   trail_features = db.relationship(
 #       TUser,
  #      backref="CW2.Trail",
   #     cascade="all, delete, delete-orphan",
    #    single_parent=True,
     #   order_by="desc(TUser.timestamp)"
    #)
    #trail_features = db.relationship(
    #    Trail_Feature,
     #   backref="TrailTest",
      #  cascade="all, delete, delete-orphan",
       # single_parent=True,
        #order_by="desc(Trail_Feature.timestamp)"
    #)
    

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sql_session = db.session
        include_fk = True
    
        
class TUser(db.Model):
    __tablename__ = "CW2.TUser"
    UserID=db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email_address=db.Column(db.String(60))
    Role=db.Column(db.String(20))
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )
    trails = db.relationship(
        Trail,
        backref="CW2.TUser",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Trail.timestamp)"
    )

class TUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TUser
        Load_instance = True
        sqla_session = db.session
        include_relationships = True
    trails = fields.Nested(TrailSchema, many=True)
        
tusers=TUserSchema(many=True)
tuser_schema = TUserSchema()
trail_schema = TrailSchema()
trails_schema = TrailSchema(many =True)
    

