import time

from sqlalchemy.sql import func

from main import db
from main.models import article_tag, Tag

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(32), nullable = False)
    content = db.Column(db.Text, nullable = False)
    click = db.Column(db.Integer, default = 0)
    support = db.Column(db.Integer, default = 0)
    create_time = db.Column(db.DateTime, server_default = func.now())
    update_time = db.Column(db.DateTime, server_default = func.now(), onupdate = func.now())
    tags = db.relationship(
        'Tag',
        secondary = article_tag,
        backref = db.backref('articles', lazy = 'dynamic'),
        lazy = 'dynamic'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'click': self.click,
            'support': self.support,
            'create_time': int(time.mktime(self.create_time.timetuple())) * 1000,
            'update_time': int(time.mktime(self.update_time.timetuple())) * 1000,
            'tags': [item.to_dict() for item in self.tags.order_by(Tag.name).all()]
        }
