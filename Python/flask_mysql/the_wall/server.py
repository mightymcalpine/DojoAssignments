import re, md5, os, binascii

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
from time import strftime

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'wall_db')
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
		flash('First Name must be at lease 2 characters, letters only', 'fname')
	if len(newUser['last_name']) < 2 or not str.isalpha(str(newUser['last_name'])):
		flash('Last Name must be at lease 2 characters, letters only', 'lname')
	# validate email and password
	if not EMAILREG.match(newUser['email']):
		flash('Sorry that was not a valid email address', 'email')	
	if not PASSWORD_REGEX.match(newUser['password']):
		flash('Password must be at least 8 characters, with at least 1 uppercase letter, lowercase letter, and number', 'password')
	if newUser['password'] != (newUser['confirm_pw']):
		flash('Passwords do not match', 'confirm_pw')
	# reset form/redirect if error messages
	if '_flashes' in session:
		return redirect('/')
	#check if email is already registered 
	check_query = "SELECT * FROM users WHERE email = :email"	
	existingUser = mysql.query_db(check_query, newUser)
	if existingUser:
		flash('The email you entered is already being used. Please try a different email or go to Login instead')
		return redirect('/')
	else:	
		newUser['pw_hash'] = bcrypt.generate_password_hash(newUser['password'])
		add_new_user_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
		addNewUser = mysql.query_db(add_new_user_query, newUser)
	# place new user in session
		session['user'] = {
				'id': addNewUser,
				'fname': newUser['first_name'],
				'lname': newUser['last_name']
			}
	# assign session keys to vars for passing into html doc
		userID = session['user']['id']
		userName = session['user']['fname']+' '+session['user']['lname']
	return redirect('/wall')

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
		# place logged in user into session
		session['user'] = {
				'id': user[0]['id'],
				'fname': user[0]['first_name'],
				'lname': user[0]['last_name']
			}
		userID = session['user']['id']
		userName = session['user']['fname']+' '+session['user']['lname']
		print 'ID HERE', userID
		print 'NAME HERE', userName
		return redirect('/wall')
	else:
		flash('Login error - Email or Password are incorrect', 'loginError')
		return redirect('/')

@app.route('/wall')
def theWall():
	userID = session['user']['id']
	userName = session['user']['fname']+' '+session['user']['lname']
	msgQuery = "SELECT messages.id AS msgID, messages.message, messages.created_at, CONCAT(users.first_name, ' ', users.last_name) AS name FROM messages JOIN users ON messages.user_id = users.id ORDER BY msgID DESC"
	postMsg = mysql.query_db(msgQuery)
	commentQuery = "SELECT comments.id, comments.comment, comments.created_at, CONCAT(users.first_name, ' ', users.last_name) AS name, message_id FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id"
	postComment = mysql.query_db(commentQuery)
	return render_template('wall.html', userName=userName, postMsg=postMsg, postComment=postComment)

@app.route('/message', methods=['POST'])
def msgPost():
	msgData = {
		'userID': session['user']['id'],
		'msg': request.form['message']
	}
	if len(msgData['msg']) < 3:
		flash('Message is too short')
		return redirect('/wall')
	else:
		msgQuery = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES(:userID, :msg, NOW(), NOW())"
		addMsg = mysql.query_db(msgQuery, msgData)
		return redirect('/wall')

@app.route('/comment/<msgID>', methods=['POST'])
def commentPost(msgID):
	commentData = {
		'userID': session['user']['id'],
		'comment': request.form['comment'],
		'messageID': msgID
	}
	if len(commentData['comment']) < 2:
		flash('Comment is too short')
		return redirect('/wall')
	else:
		commentQuery = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES(:userID, :messageID, :comment, NOW(), NOW())"
		addComment = mysql.query_db(commentQuery, commentData)
		return redirect('/wall')

@app.route('/logout', methods=['GET'])
def logout():
	session.clear()
	flash('You have been logged out')
	return redirect('/')

app.run(debug=True, port=5151)