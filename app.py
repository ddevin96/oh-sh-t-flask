import base64
from flask import Flask, request
from flask_cors import CORS, cross_origin
from keras.models import load_model
from tensorflow_addons.optimizers import AdamW
from transformers import AutoTokenizer, TFRobertaModel
import transformers
import re

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = load_model("model32_0.35_1e-05_5e-07.h5", custom_objects={"TFRobertaModel": transformers.TFRobertaModel})

@app.route("/predictline", methods=["POST"])
@cross_origin()
def predict_line():
    j = request.get_json()
    t = j.get("textToAnalyze")
    # base64 decode
    t = base64.b64decode(t).decode("utf-8")
    string = remove_emojis(t)
    x = (string
        .lower()     
        .replace('\x89Ûª|�Ûª', "'")
        .replace('\n|\x89.|\x9d *', ' ')
        .replace('&gt;', ">")
        .replace('&lt;', "<")
        .replace('&amp;', " and ")
        .replace('won\'t', 'will not')
        .replace('can\'t', 'cannot')
        .replace('i\'m', 'i am')
        .replace('ain\'t', 'is not')
        .replace('hwy.', 'highway')
        .replace('(\w+)\'ll', '\g<1> will')
        .replace('(\w+)n\'t', '\g<1> not')
        .replace('(\w+)\'ve', '\g<1> have')
        .replace('(\w+)\'s', '\g<1> is')
        .replace('(\w+)\'re', '\g<1> are')
        .replace('(\w+)\'d', '\g<1> would')     
        .replace('(\w+)\'m', '\g<1> am')
        .replace('<3', 'love')
        .replace('w/e', 'whatever')
        .replace('w/', 'with')    
        .replace('\b', ' ')
        .replace('-', ' ')
        .replace('  *', ' ')
        )

    tokenizer = AutoTokenizer.from_pretrained('vinai/bertweet-base', 
                            normalization=True, 
                            use_fast = False,
                            add_special_tokens=True,
                            pad_to_max_length=True,
                            return_attention_mask=True)
    token = tokenizer(string, 
                    padding="max_length", 
                    truncation=True,
                    return_tensors = 'tf').data
    
    prediction = model.predict(token)

    if prediction[0][0] < 0.5:
        print(" < 0.5 Prediction:", prediction[0][0])
        return {
            "malignant": True
        }
    else:
        print(" > 0.5 Prediction:", prediction[0][0])
        return {
            "malignant": False
        }
    
# @app.route("/predictline", methods=["POST"])
# @cross_origin()
# def predict_line():
#     j = request.get_json()
#     # pick value from json
#     t = j.get("textToAnalyze")
#     # base64 decode
#     t = base64.b64decode(t).decode("utf-8")
#     print(t)
#     return {
#         "malignant": True
#     }

@app.route("/predictpage", methods=["POST"])
def predict_page():
    j = request.get_json()
    print(j)
    return {
        "prediction": "Predicted page!!"
    }

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)