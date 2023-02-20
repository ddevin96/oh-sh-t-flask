import base64
from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/predictline", methods=["POST"])
@cross_origin()
def predict_line():
    j = request.get_json()
    # pick value from json
    t = j.get("textToAnalyze")
    # base64 decode
    t = base64.b64decode(t).decode("utf-8")
    print(t)
    return {
        "malignant": True
    }

@app.route("/predictpage", methods=["POST"])
def predict_page():
    j = request.get_json()
    print(j)
    return {
        "prediction": "Predicted page!!"
    }