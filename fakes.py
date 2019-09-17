'''
生成虚拟数据
'''
from faker import Faker

from MyBlog.models import Admin, Category, Ports, Comments
from MyBlog.extensions import db
from sqlalchemy.exc import IntegrityError
import random

# 生成假管理员
def fake_admin():
    admin = Admin(
        username='admin',
        blog_title='MyBlog',
        blog_sub_title='MyBlog is very well!',
        name='Lxiin00',
        about='This is my first Blog!!!'
    )
    admin.set_password('MyBlog')
    db.session.add(admin)
    db.session.commit()

fake = Faker()

# 生成假文章分类（默认+10个）
def fake_category(count=10):
    category = Category(name='Default')
    db.session.add(category)

    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

# 生成假文章（50篇）
def fake_posts(count=50):
    for i in range(count):
        posts = Ports(
            title=fake.sentence(),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(posts)
    db.session.commit()

def fake_comments(count=500):
    for i in range(count):
        comments = Comments(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            posts=Ports.query.get(random.randint(1, Ports.query.count()))
        )
        db.session.add(comments)

    # 未审核评论
    salt = int(count * 0.1)
    for i in range(salt):
        comments = Comments(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year(),
            reviewed=False,
            posts=Ports.query.get(random.randint(1, Ports.query.count()))
        )
        db.session.add(comments)

