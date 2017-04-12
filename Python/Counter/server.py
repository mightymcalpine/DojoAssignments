from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key = 'super1984secret'



@app.route('/')
def index():
	counter = session['pageCount']	
	print counter
	return render_template('index.html', counter=counter)

@app.route('/counter', methods=['POST'])
def counter():
	session['pageCount'] += 2
	return redirect('/')
	
@app.route('/reset', methods=['POST'])
def reset():
	session['pageCount'] = 0
	return redirect('/')

app.run(debug=True, port=8888)