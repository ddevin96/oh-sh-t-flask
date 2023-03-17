# info

project for Ph.D. course CITR
refer also to
- Chrome extension [oh-shi-t](https://github.com/piscitelli91/oh-sh-t)
- AI Model [model](https://github.com/gilbertrec/TR_CI2023-CyberBullying)

# setup for Flask

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
- output: {"malignant": boolean}
  - if output > 0.5 return true, meaning text is malignant

WIP -- POST API -- http://127.0.0.1:5000/predict_page

