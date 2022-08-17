from app import db

from datetime import datetime

from werkzeug.security import generate_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.string(50), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Save the password as the hashed version of the password
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    relationship = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.string(50), nullable = False)
    phone_number = db.Column(db.string(25), nullable = False)
    home_address = db.Column(db.string(75), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()