import re, datetime

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from time import strftime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,20}$')

app = Flask(__name__)
app.secret_key='secretsauce81'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/registration', methods=['POST'])
def registration():
	session['firstname'] = request.form['firstname']
	session['lastname'] = request.form['lastname']
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['confirm'] = request.form['confirm']
	session['birthday'] = request.form['birthday']
	today = datetime.datetime.today()
	print today
	
	if len(session['firstname']) > 1 and str.isalpha(str(session['firstname'])):
		pass
	else:
		flash('First name required, letters only please')		
	if len(session['lastname']) > 1 and str.isalpha(str(session['lastname'])):
		pass
	else:
		flash('Last name required, letters only please')

	# if session['birthday'] > today:
	# 	flash("INVALID Date, registrants must not be from the future")

	if len(session['email']) < 1:
		flash('Email required')
	elif not EMAIL_REGEX.match(session['email']):
		flash('NOT A VALID EMAIL ADDRESS')
	else:
		pass
	if not PASSWORD_REGEX.match(session['password']):
		flash('Password must be between 8-16 characters, contain at least 1 uppercase letter, lowercase letter, and number')
	elif session['password'] != session['confirm']:
		flash('Password does not match, please try again')
	if '_flashes' not in session:
		flash('Thank you for registering for the Revolution')
	return redirect('/')

app.run(debug=True, port=9191)