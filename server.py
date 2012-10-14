import os
from flask import Flask, Response, request, json, render_template
from flask.ext.pymongo import PyMongo

# phone number is (424) 231-5779

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://user:password@ds039717.mongolab.com:39717/heroku_app8402029"

mongo = PyMongo(app)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/json")
def votesAsJSON():
    data = {
        "A": mongo.db.votes.find({"to": "A"}).count(),
        "B": mongo.db.votes.find({"to": "B"}).count()
    }

    return Response(json.dumps(data), mimetype="application/json")

@app.route("/vote", methods=["post"])
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