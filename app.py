from flask import Flask, request

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/predictline", methods=["POST"])
def predict_line():
    j = request.get_json()
    # pick value from json
    t = j.get("textToAnalyze")
    print(t)
    return {
        "prediction": "Predicted line!!"
    }

@app.route("/predictpage", methods=["POST"])
def predict_page():
    j = request.get_json()
    print(j)
    return {
        "prediction": "Predicted page!!"
    }