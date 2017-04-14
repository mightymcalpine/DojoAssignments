from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from random import randint

app = Flask(__name__)
app.secret_key = 'secretsauce81'

@app.route('/')
def index():
	if 'randomNum' not in session:
		session['randomNum'] = randint(1, 100)	
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def userGuess():
	guess = int(request.form['guess'])	
	if guess > session['randomNum']:
		print "guess too high"
		session['guess'] = 'too HIGH'
	elif guess < session['randomNum']:		
		session['guess'] = 'too LOW'
	else:		
		session['guess'] = 'Winner!'
	return redirect('/')

@app.route('/reset', methods=['GET'])
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True, port=8517)