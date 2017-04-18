import re

from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'ShazzyHiddenDojo'

@app.route('/')
def index():
	return render_template('index.html')
# this route will handle our form submission

@app.route('/users', methods=['POST'])
# notice how we defined which HTTP methods are allowed by this route
def create_user():
		# assign form values to session keys
	session['name'] = request.form['name']	
	session['email'] = request.form['email']
	
	if len(session['name']) < 2:
		flash('{} is not a valid name, too short'.format(session['name']))
	else:
		flash('Success, good job on your own name')
	if len(session['email']) < 1:
		flash('email field cannot be blank')
	elif not EMAIL_REGEX.match(session['email']):
		flash('NOT A VALID EMAIL ADDRESS')
	else:
		flash('Success')
	   
	
	return redirect('/')
	# return render_template('users.html', name=name, email=email)
# redirects back to the '/' server

@app.route('/show')
def users():
	return render_template('users.html')
	
app.run(debug=True, port=8585)
# run our server