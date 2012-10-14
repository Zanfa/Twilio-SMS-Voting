import os
from flask import Flask, Response, request
from flask.ext.pymongo import PyMongo

# phone number is (424) 231-5779

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://user:password@ds039717.mongolab.com:39717/heroku_app8402029"

mongo = PyMongo(app)

@app.route('/')
def main():
    return "Votes for A: " + str(mongo.db.votes.find({"to": "A"}).count()) + \
           " Votes for B: " + str(mongo.db.votes.find({"to": "B"}).count())

@app.route('/vote', methods=['post'])
def vote():
    msg = request.form["Body"]

    mongo.db.votes.insert({
        "to": request.form["Body"],
        "from": request.form["From"]
    });

    return Response("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n", mimetype="text/xml")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)