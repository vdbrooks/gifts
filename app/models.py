from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    giftees = db.relationship('Giftee', backref='gifter', lazy='dynamic')
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('Bro, you\'re not allowed to read plain text passwords')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha512',salt_length=64)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Giftee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=False)
    gender = db.Column(db.String(7), unique=False)
    age = db.Column(db.Integer, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Giftee %r>' % (self.nickname)


