from flask import Flask, json,session
from flask_serialize.flask_serialize import FlaskSerialize,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlalchemy
from flask_restful import Resource, Api


app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
api=Api(app)

from models import Hashtag, Tweet

#fs_mixin=FlaskSerialize(db)

class Home(Resource):
    def get(self):
        return {'Available Endpoints': {
            'GET': 'http://127.0.0.1:8080/tweet',
            'POST': 'http://127.0.0.1:8080/trending-hashtags'
        }
        }

class Tweets(Resource):
    def post(self):
        data=request.json
        tweet=Tweet(tweet=data['tweet'])
        try:
            db.session.add(tweet)
            db.session.commit()
        except Exception:
            return jsonify("Tweet already exists.")
        hashtags=data['tweet'].split('#')
        for i in hashtags[1:]:
            try:
                db.session.flush()
                ht=Hashtag(hashtag=i.strip(),hashtags_count=1)
                db.session.add(ht)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                count=Hashtag.query.filter_by(hashtag=i.strip()).first()
                count.hashtags_count+=1
                db.session.commit()
        return jsonify("sucess: data received")

class Hashtags(Resource):
    def get(self):
        hashtags=Hashtag.query.order_by(Hashtag.hashtags_count.desc()).limit(25).with_entities(Hashtag.hashtag).all()
        if len(hashtags)==0: 
            return jsonify("No hashtags available. Please add tweets!! ")
        hashtags=[i[0] for i in hashtags]
        return {"hashtags":hashtags}

api.add_resource(Home,'/')
api.add_resource(Tweets,'/tweet')
api.add_resource(Hashtags,'/trending-hashtags')


        

if __name__ == "__main__":
    app.run(debug=True,port=8080)