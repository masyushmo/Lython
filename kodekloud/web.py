from flask import Flask
from redis import Redis

app = Flask(__name__)
redisdb = Redis(host="127.0.0.1",port=6379) 

@app.route('/')

def welcomePage():
    redisdb.incr('VisitCount')
    visitCount = str(redisdb.get('VisitCount'), 'utf-8')
    return "Hello Web! Visitors count: " + visitCount

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)