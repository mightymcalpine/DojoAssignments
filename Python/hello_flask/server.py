import math, random


from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"
	return render_template('index.html')

app.run(debug=True, port=8888)
# must have, run once at the end of script