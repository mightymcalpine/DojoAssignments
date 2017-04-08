from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html', phrase='Force Power Rising', times=5)
app.run(debug=True, port=8888)
