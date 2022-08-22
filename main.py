from flask import Flask, request
from collections import Counter

app = Flask(__name__)

def count_chars(word):
    count = Counter(word)
    return count


@app.route("/")
def hello_world():
    return count_chars('some word')
    return "<p>Hello, World!</p>"

@app.route("/count", methods=["POST"])
def count_words():
    return {'word':request.form['word']}