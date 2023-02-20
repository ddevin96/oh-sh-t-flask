# info

project for phd course CITR --
refer also to
https://github.com/piscitelli91/oh-sh-t
https://github.com/gilbertrec/TR_CI2023-CyberBullying

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

- input: {"textToAnalyze": "text"}
- output: {"prediction": "0"}

POST API -- http://127.0.0.1:5000/predict_page

- input: {"texts": ["text1", "text2"]}
- output: {"predictions": ["0", "1"]}

