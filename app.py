from flask import Flask
from redis import Redis
import sys
app = Flask(__name__)
redis = Redis(host="redis")

@app.route("/")
def hello():
	visits = redis.incr('counter')
	html = "<h3>Hello World!</h3><b>Visits:</b> {visits}<br/>"
	print("Test console")
	return 1
   # return html.format(visits=visits)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    sys.exit()

