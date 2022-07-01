from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(200))
    role = db.Column(db.String(50))


class UserSchema(Schema):
    __tablename__ = 'user'

    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
