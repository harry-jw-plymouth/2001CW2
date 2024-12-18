# models.py

from datetime import datetime
import pytz

from config import db, ma


class Trail(db.Model):
    __tablename__ = "TrailTest"
    TrailId=db.Column(db.Integer, primary_key=True)
    Trail_name=db.Column(db.String(60), unique=True)
    Trail_Summary=db.Column(db.String(6000))
    Trail_Description=db.Column(db.String(6000))
    Difficulty=db.Column(db.String(10))
    Location=db.Column(db.String(100))
    Length=db.Column(db.Float)
    Elevation_gain=db.Column(db.Float)
    Route_type=db.Column(db.String(10))
    OwnerID=db.Column(db.Integer)
    timestamp = db.Column(
        db.DateTime, default=lambda: datetime.now(pytz.timezone('Europe/London')),
        onupdate=lambda: datetime.now(pytz.timezone('Europe/London'))
    )
    

class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sql_session = db.session

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
    

