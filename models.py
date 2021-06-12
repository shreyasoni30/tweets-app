from __main__ import db


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(200), unique=True, nullable=False)
     
    create_fields=update_fields=['tweet']

    def __repr__(self):
        return '<Tweet %r>' % self.id

class Hashtag(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    hashtag= db.Column(db.String(200), unique=True, nullable=False)
    hashtags_count=db.Column(db.Integer)

    def __repr__(self):
        return '<HashTag %r>' % self.id

db.create_all()
db.session.commit()