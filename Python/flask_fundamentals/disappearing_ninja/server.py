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
	return render_template('index.html')

@app.route('/ninjas')
def all_ninjas():
	color = 'none'
	return render_template('ninjas.html', color=color)

@app.route('/ninjas/<color>')
def color_ninja(color):
	ninja = ''
	if color == 'blue':
		ninja = 'leonardo'
	elif color == 'purple':
		ninja = 'donatello'
	elif color == 'red':
		ninja = 'raphael'
	elif color == 'orange':
		ninja = 'michelangelo'
	else:
		ninja = 'notapril'
	return render_template('ninjas.html', ninja=ninja)


app.run(debug=True, port=8888)