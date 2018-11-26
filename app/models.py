from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    full_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    bio = db.Column(db.String(150))
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(256))
    post = db.relationship('Post', backref=db.backref('user', lazy='joined'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User {} is {}' .format(self.username, self.age)









class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tweet = db.Column(db.String(140))
    date = db.Column(db.DateTime, default=datetime.now().date())
    likes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return 'Post {} by {}: {}' .format(self.id, self.name, self.tweet)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
