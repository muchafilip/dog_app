from datetime import datetime

from flask_bcrypt import check_password_hash, generate_password_hash

from .db import db


class Marker(db.Document):
    name = db.StringField(required=True, unique=True)
    date_modified = db.DateTimeField(default=datetime.utcnow)
    coord = db.PointField(db.StringField(), required=True)
    tags = db.ListField(db.StringField(), required=False)
    added_by = db.ReferenceField('User')


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    markers = db.ListField(db.ReferenceField(
        'Marker', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Marker, 'added_by', db.CASCADE)
