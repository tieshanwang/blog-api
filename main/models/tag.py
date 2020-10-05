import time

from sqlalchemy.sql import func

from main import db

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), unique = True, nullable = False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
