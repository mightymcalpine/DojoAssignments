import re

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from mysqlconnection import MySQLConnector
from time import strftime

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
app.secret_key = 'secretsauce81'
EMAILREG = re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
	data = {'email': request.form['email']}
	if EMAILREG.match(data['email']):
		query = "INSERT INTO email (email, created_at, updated_at) VALUES(:email, NOW(), NOW())"
		mysql.query_db(query, data)
		query_all = "SELECT email, created_at FROM email"
		all_email = mysql.query_db(query_all)
		return render_template('success.html', all_email=all_email, email=data)
	else:
		flash('NOT A VALID EMAIL. Please Try Again')
		return redirect('/')

app.run(debug=True, port=8222)