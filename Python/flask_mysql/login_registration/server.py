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
app.secret_key='secretsauce81'
EMAILREG = re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*[^a-zA-Z])(?=.*[a-z])(?=.*[A-Z])\S{8,255}$')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/newAccount', methods=['POST'])
def newAccount():
	password = request.form['password']
	newUser = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email'],
		'password': password,
		'confirm_pw': request.form['confirm_pw'],
		'encrypted_pw': bcrypt.generate_password_hash(password)
	}
	if len(newUser['first_name']) < 2 or not str.isalpha(str(newUser['first_name'])):
		flash('First Name must be at lease 2 characters, letters only')
	if len(newUser['last_name']) < 2 or not str.isalpha(str(newUser['last_name'])):
		flash('Last Name must be at lease 2 characters, letters only')
	if not EMAILREG.match(newUser['email']):
		flash('Email must be valid email address')
	email_query = "SELECT id FROM users WHERE email = :email"
	check_email = mysql.query_db(email_query, newUser)
	if check_email:
		flash('The email you entered is already being used. Please try again')
	if not PASSWORD_REGEX.match(newUser['password']):
		flash('Password must be at least 8 characters, with at least 1 uppercase letter, lowercase letter, and number')
	if newUser['password'] != (newUser['confirm_pw']):
		flash('Passwords do not match')
	if '_flashes' in session:
		return redirect('/')
	insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :encrypted_pw, NOW(), NOW())"
	user = mysql.query_db(insert_query, newUser)
	
	session['id'] = str(check_email[0]['id'])
	print 'HERE', session['id']
	return render_template('newaccount.html', newUser=newUser)

@app.route('/login/<id>', methods=['POST'])
def login(id):
	email = request.form['email']
	password = request.form['password']
	
	
	return render_template('users.html', id=id)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

app.run(debug=True, port=8181)