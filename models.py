from MyBlog.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


# 管理员
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), index=True)
    password_hash = db.Column(db.String(128))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(100))
    name = db.Column(db.String(30))
    about = db.Column(db.Text)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

# 文章分类
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)

    ports = db.relationship('Ports', back_populates='category')

# 文章
class Ports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    can_comment = db.Column(db.Boolean, default=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='ports')

    comments = db.relationship('Comments', back_populates='ports', cascade='all, delete-orphan')

# 文章评论
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(254))
    site = db.Column(db.String(255))
    body = db.Column(db.Text)
    from_admin = db.Column(db.Boolean, default=False)
    reviewed = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    posts_id = db.Column(db.Integer, db.ForeignKey('ports.id'))
    posts = db.relationship('Post', back_populates='comments')

    replied_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    replies = db.relationship('Comments', back_populates='replied', cascade='all, delete-orphan')
    replied = db.relationship('Comments', back_populates='replies', remote_side=[id])