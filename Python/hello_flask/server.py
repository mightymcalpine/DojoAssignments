import math, random

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session

app.secret_key = 'manysecrets1984'


app = Flask(__name__)

@app.route('/')
def hello():
	name = 'Lars'
	age = 35
	return render_template('index.html', name ='Lars', age=age)

@app.route('/numbers')
def numbers():
	for number in range(3):
		print "We're in numbers"
	return redirect('/')

@app.route('/flexbox')
def flexbox():
		return render_template('flexbox.html')	
	

app.run(debug=True, port=8888)
# must have, run once at the end of script