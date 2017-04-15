from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key='secretsauce81'

@app.route('/')
def index():
	if 'flash' in session:
		flash.clear()		
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	# name = request.form['name']
	# location = request.form['location']
	# language = request.form['language']
	# comments = request.form['comments']
	
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comments'] = request.form['comments']
	
	if len(session['name']) == 0 or len(session['comments']) == 0:
		flash('*** Name and Comment fields required ***')
		return redirect('/')
		
	if len(session['comments']) > 120:
		flash('*** Comments limited to 120 characters ***')
		return redirect('/')
	else:
		pass
	
	
	return render_template('results.html')


app.run(debug=True, port=8686)