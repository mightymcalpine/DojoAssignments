from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comments = request.form['comments']
	print name, location, language, comments
	return render_template('results.html', name=name, location=location, language=language, comments=comments)


app.run(debug=True, port=8686)