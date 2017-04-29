import re

from datetime import datetime
from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'users_db')
app.secret_key = 'manysecrets1984'
rightnow = datetime.now()
print 'time is', rightnow
EMAILREG = re.compile(r'^[a-zA-Z0-9\.\+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')

@app.route('/')
def hello():
	query_all = "select * FROM users_db.users"
	all_users = mysql.query_db(query_all)
	return render_template('index.html', all_users=all_users)

@app.route('/user', methods=['POST'])
def addUser():
	user_info = {
	'first_name': request.form['fname'],
	'last_name': request.form['lname'],
	'email': request.form['email']
	}
	
	if len(user_info['first_name']) <= 2:
		flash('<p>First Name must be longer than 2 characters</p>')
	if len(user_info['last_name']) <= 2:
		flash('<p>Last Name must be longer than 2 characters</p>')
	if not EMAILREG.match(user_info['email']):
		flash('<p>Email must be valid email address</p>')
	if '_flashes' in session:
		return redirect('/')
	
	newUser_query = "INSERT INTO users(first_name, last_name, email, created_at, update_at) VALUES (:first_name, :last_name, :email, now(), now());"
	newUser = mysql.query_db(newUser_query, user_info)
	return redirect('/')
	
@app.route('/user/<id>')
def showUser(id):
	one_user_query = "SELECT id, first_name, last_name, email FROM users WHERE id = :id"
	one_user_data = {
		"id": id
	}
	one_user = mysql.query_db(one_user_query, one_user_data)
	print one_user
	return render_template('user.html', user=one_user[0])	

@app.route('/user/update/<id>')
def showUpdate(id):
	one_user_query = "SELECT id, first_name, last_name, email FROM users WHERE id = :id"
	one_user_data = {
		"id": id
	}
	one_user = mysql.query_db(one_user_query, one_user_data)
	return render_template('edit.html', user=one_user[0])

@app.route('/user/update/<id>', methods=['POST'])
def update(id):
	update_query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, update_at = now() WHERE id = :id"
	update_data = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email'],
		'id': id
	}
	mysql.query_db(update_query, update_data)
	return redirect('/user/' + id)

@app.route('/user/delete/<id>', methods=['GET'])
def deleteCheck(id):
	one_user_query = "SELECT id, first_name, last_name, email FROM users WHERE id = :id"
	one_user_data = {
		"id": id
	}
	one_user = mysql.query_db(one_user_query, one_user_data)
	return render_template('delete.html', user=one_user[0])

@app.route('/user/delete', methods=['POST'])
def delect():
	delete_query = "DELETE FROM users WHERE id = :id"
	delete_data = {
		"id": request.form['user_id']
	}
	mysql.query_db(delete_query, delete_data)
	flash('user has been successfully deleted')
	return redirect('/')

@app.route('/clear')
def clearSession():
	session.clear()
	return redirect('/')

app.run(debug=True, port=8585)
# must have, run once at the end of script