# setup

- MacOS
    - ```sh
        python3 -m venv venv
        . venv/bin/activate
        pip install Flask
        ```
# running

```sh 
. venv/bin/activate
flask run
```

# structure of API

POST API -- http://127.0.0.1:5000/predict_line
input: {"textToAnalyze": "text"}
output: {"prediction": "text"}

POST API -- http://127.0.0.1:5000/predict_page
input: {?}
output: {?}