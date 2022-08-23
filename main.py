from flask import Flask, request
from collections import Counter
from rq import Queue
from redis import Redis
from rq.job import Job

conn = Redis('localhost', 6379, charset="utf-8")

q = Queue(connection=conn)

app = Flask(__name__)

def count_chars(word):
    count = Counter(word)
    print(count)
    return count


@app.route("/")
def hello_world():
    return count_chars('some word')
    return "<p>Hello, World!</p>"

@app.route("/count", methods=["POST"])
def count_words():
    result = q.enqueue(count_chars, request.form['word'])
    print(result.get_id())
    return {'count':'result'}

@app.route("/result", methods=["GET"])
def get_result():
    args = request.args.to_dict()
    job = Job.fetch(args.get("job_key"), connection=conn)
    if job.is_finished:
        return job.result, 200
    else:
        return "Nay!", 202
