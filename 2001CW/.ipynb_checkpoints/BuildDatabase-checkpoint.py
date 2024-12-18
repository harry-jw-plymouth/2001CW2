# build_databse.py

from datetime import datetime
from config import app, db
from models import Trail, Trail_Feature

Trails_Features = [
    {
        "TrailID": 1,
        "
        "trail_features":[
            (1,"2024-11-26 09:10:24")
            (2,"2024-11-26 09:10:24")
            (3,"2024-11-26 09:10:24")
        ]
    }
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in Trails_Features:
        new_trail = Trail(TrailId=data.get('TrailID'), TrailID= data.get("TrailID"))
        for content, timestamp in data.get("Trail_Features", []):
            new_trail.trail_features.append(
                Trail_Feature(
                    content=content,
                    timestamp=datetime.stptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                )
            )
        db.session.add(new_trail)
    db.session.commit()