# Twitter Trending Hashtags

This application  have two REST endpoints . The first endpoint will receive a series of tweet-like requests. The second endpoint will return a list of the top 25 hashtags in descending order.


### Endpoints :

- `POST` **/tweet** - Create tweet. Takes a json ({"tweet": your_tweet})
- `GET` **/trending-hashtags** - Returns a list of top 25 trending hashtags.
<br>
  
## Getting Started
Follow the instruction to setup the Flask application on your local system.

## Create Virtual Environment
```
virtialenv venv
source venv/bin/activate
```

## Install Requirements
```
pip install -r requirements.txt
```

## To run the program in local server use the following command
```
python app.py
Then go to http://127.0.0.1:8080/ in your browser
```

### To populate the database with some initial tweets run the bash file.
```
./tweets.sh
```




