from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_password = db.Column(db.String(128), nullable=False)
    deals = db.relationship('Deal', backref='author', lazy=True)

    # Only keep this:
    liked_deals = db.relationship('DealLike', back_populates='user', cascade='all, delete-orphan')

    def set_password(self, password):
        self.user_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.user_password, password)

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    def has_liked(self, deal):
        return any(like.deal_id == deal.deal_id for like in self.liked_deals)

    def like_deal(self, deal):
        if not self.has_liked(deal):
            db.session.add(DealLike(user_id=self.user_id, deal_id=deal.deal_id))
            db.session.commit()

    def unlike_deal(self, deal):
        like = DealLike.query.filter_by(user_id=self.user_id, deal_id=deal.deal_id).first()
        if like:
            db.session.delete(like)
            db.session.commit()

    

class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    dob = db.Column(db.Date)
    gender = db.Column(db.String(1))
    num_likes = db.Column(db.Integer, default=0)

class Deal(db.Model):
    __tablename__ = 'deals'
    deal_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    deal_desc = db.Column(db.Text, nullable=False)
    promo_code = db.Column(db.String(100), nullable=True)
    deal_entered = db.Column(db.Date, default=datetime.utcnow)
    deal_validity = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    store = db.relationship('Store', backref='deals', lazy=True)
    category = db.relationship('Category', backref='deals', lazy=True)

    # Only keep this:
    likes = db.relationship('DealLike', back_populates='deal', cascade='all, delete-orphan')


    def __repr__(self):
        return f"Deal('{self.deal_desc}', '{self.deal_entered}')"



class Store(db.Model):
    __tablename__ = 'stores'
    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.Text, nullable=False)

class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.Text, nullable=False)
    category_desc = db.Column(db.Text)
    
class DealLike(db.Model):
    __tablename__ = 'deal_likes'
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    deal_id = db.Column(db.Integer, db.ForeignKey('deals.deal_id'), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Only these two:
    user = db.relationship('User', back_populates='liked_deals')
    deal = db.relationship('Deal', back_populates='likes')




