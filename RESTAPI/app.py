from flask import Flask, jsonify, Response
import redis
import json

app = Flask(__name__)

cache = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

@app.route("/")
def index():
    # fetch everything that is in response_times list
    data = cache.lrange("response_times", 0, -1)
    return Response(json.dumps(data), mimetype='application/json')
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)