from main import db

article_tag = db.Table(
    'article_tag', 
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id')), 
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)
