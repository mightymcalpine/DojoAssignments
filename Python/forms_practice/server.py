from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session


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
	print 'Got POST info'
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	# print name
	return redirect('/show')
	# return render_template('users.html', name=name, email=email)
# redirects back to the '/' server

@app.route('/show')
def users():
	return render_template('users.html')
	
app.run(debug=True, port=8585)
# run our server