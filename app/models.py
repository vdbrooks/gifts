from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(320), unique=False)
    giftees = db.relationship('Giftee', backref='user', lazy='dynamic')

    #def __init__(self, username, email, password):
    #    self.username = username
    #    self.email = email
    #    self.password = password
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


