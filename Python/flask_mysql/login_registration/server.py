import re, md5, os, binascii

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_reg')
app.secret_key='Bsn72sbtqC8TX&R8szc?'
EMAILREG = re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,255}$')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/register', methods=['POST'])
def newAccount():
	# Grab user data from the registration form
	newUser = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email'],
		'password': request.form['password'],
		'confirm_pw': request.form['confirm_pw']
	}
	# validate name
	if len(newUser['first_name']) < 2 or not str.isalpha(str(newUser['first_name'])):
		flash('First Name must be at lease 2 characters, letters only')
	if len(newUser['last_name']) < 2 or not str.isalpha(str(newUser['last_name'])):
		flash('Last Name must be at lease 2 characters, letters only')
	# validate email and password
	if not EMAILREG.match(newUser['email']):
		flash('Email must be valid email address')	
	if not PASSWORD_REGEX.match(newUser['password']):
		flash('Password must be at least 8 characters, with at least 1 uppercase letter, lowercase letter, and number')
	if newUser['password'] != (newUser['confirm_pw']):
		flash('Passwords do not match')
	# reset form/redirect if error messages
	if '_flashes' in session:
		return redirect('/')
	#check if email is already registered 
	check_query = "SELECT id, email FROM users WHERE email = :email"	
	existingUser = mysql.query_db(check_query, newUser)
	if existingUser:
		flash('The email you entered is already being used. Please try a different email or go to Login instead')
		return redirect('/')
	else:	
		newUser['pw_hash'] = bcrypt.generate_password_hash(newUser['password'])
		add_new_user_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
		addNewUser = mysql.query_db(add_new_user_query, newUser)
	# place new user in session
	session['id'] = addNewUser
	userID = session['id']

	return render_template('newaccount.html')

@app.route('/login', methods=['POST'])
def login():
	# grab user data from login form
	userData = {
		'email': request.form['email'],
		'pw_hash': request.form['password']
	}
	# check email and password
	user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	user = mysql.query_db(user_query, userData)
	if user and bcrypt.check_password_hash(user[0]['password'], userData['pw_hash']):
		return render_template('users.html')
	else:
		flash('login attempt failed')
		return redirect('/')

app.run(debug=True, port=8181)