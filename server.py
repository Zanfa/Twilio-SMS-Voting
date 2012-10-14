import os
from flask import Flask, Response
from flask.ext.pymongo import PyMongo

# phone number is (424) 231-5779

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://user:password@ds039717.mongolab.com:39717/heroku_app8402029"

mongo = PyMongo(app)

@app.route('/', methods=['get', 'post'])
def hello():
    return Response("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Response><Sms>Hello, Mobile Monkey</Sms></Response>",
        mimetype="text/xml")

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)