from .db import db
from datetime import datetime


class Marker(db.Document):
    name = db.StringField(required=True, unique=True)
    author = db.StringField(required=True, unique=False)
    date_modified = db.DateTimeField(default=datetime.utcnow)
    coord = db.PointField(db.StringField(), required=True)
    tags = db.ListField(db.StringField(), required=False)
