import re

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friends_db')
app.secret_key="secretsauce81"
EMAILREG = re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	all_friends = mysql.query_db(query)
	return render_template('index.html', all_friends=all_friends)

@app.route('/friends', methods=['POST'])
def created():
	friend_data = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email']
	}
	if len(friend_data['first_name']) < 2:
		flash('First Name must be at lease 2 characters')
	if len(friend_data['last_name']) < 2:
		flash('Last Name must be at lease 2 characters')
	if not EMAILREG.match(friend_data['email']):
		flash('Email must be valid email address')
	if '_flashes' in session:
		return redirect('/')
	query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())"
	mysql.query_db(query, friend_data)
	return redirect('/')

@app.route('/friend/<id>/edit', methods=['GET'])
def edit(id):
	query = 'SELECT id, first_name, last_name, email FROM friends WHERE id=:id'
	friend_data = {
		'id': id
	}
	one_friend = mysql.query_db(query, friend_data)
	return render_template('edit_friend.html', friend=one_friend[0])

@app.route('/friend/<id>', methods=['POST'])
def update(id):
	friend_data = {
		'first_name': request.form['fname'],
		'last_name': request.form['lname'],
		'email': request.form['email'],
		'id': id
	}
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
	mysql.query_db(query, friend_data)
	return redirect('/')

@app.route('/friend/<id>/confirm', methods=['GET'])
def deleteConfirmation(id):
	query = 'SELECT id, first_name, last_name, email FROM friends WHERE id=:id'
	friend_data = {
		'id': id
	}
	delete_friend = mysql.query_db(query, friend_data)
	return render_template('delete_friend.html', friend=delete_friend[0])

@app.route('/friend/<id>/delete', methods=['POST'])
def destroy(id):
	query = 'DELETE FROM friends WHERE id = :id'
	friend_data = {'id': id}
	mysql.query_db(query, friend_data)
	flash('Goodbye friend')
	return redirect('/')

app.run(debug=True, port=8517)