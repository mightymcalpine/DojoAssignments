from flask import Flask
from flask import redirect
from flask import render_template
from flask import request


app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
	return render_template('index.html')
# this route will handle our form submission

@app.route('/users', methods=['POST'])
# notice how we defined which HTTP methods are allowed by this route
def create_user():
	print 'Got POST info'
	name = request.form['name']
	email = request.form['email']
	return redirect('/')
# redirects bakc to the '/' server

app.run(debug=True, port=8585)
# run our server