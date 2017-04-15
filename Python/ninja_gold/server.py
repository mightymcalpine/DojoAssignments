from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from random import randint
from time import strftime
# Sublime is forcing each import statement to its own line, still trying to resolve this issue

app = Flask(__name__)
app.secret_key="secretsauce81"

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
	if 'warchest' not in session:
		session['warchest'] = 0
	if 'game_log' not in session:
		session['game_log'] = []
	return render_template('index.html')
	
@app.route('/process_money', methods=['POST'])
def gold_calc():
	session['warchest'] = session['gold']
	if request.form['building'] == 'farm':		
		session['gold'] += randint(10, 20)		
		if session['gold'] > 100:
			flash('You have quite a bit of gold now, perhaps you should try your luck at the casino')
	elif request.form['building'] == 'cave':		
		session['gold'] += randint(5, 10)
	elif request.form['building'] == 'house':			
		session['gold'] += randint(2, 5)
	elif request.form['building'] == 'casino' and session['warchest'] == 0:	
		flash('Casino has a 5 gold cover, come back when you have at least 5 gold')
	elif request.form['building'] == 'casino' and session['warchest'] < -100:
		flash('You are now 100 golds in debt, time for you to get some more gold before we let you play here again')	
	elif request.form['building'] == 'casino':			
		winLossRatio = randint(1, 100)
		if winLossRatio <= 40:
			session['gold'] += randint(0, 50)
		else:
			session['gold'] -= randint(0, 50)
		
	session['building'] = request.form['building']
	session['gold_this_rnd'] = session['gold'] - session['warchest']
	session['time_date'] = strftime("%I:%M:%S")

	if session['gold_this_rnd'] > 0:
		session['game_log'].append('<p id="win-msg">' + 'You won ' + str(session['gold_this_rnd']) + ' gold from the ' + session['building'] + ' ' + session['time_date'] + '</p>')
	elif session['gold_this_rnd'] < 0 and session['building'] == 'casino':
		session['game_log'].append('<p class="fail-msg">' + 'Bummer you lost ' + str(session['gold_this_rnd']) + ' gold from the ' + session['building'] + ' ' + session['time_date'] + '</p>')
	return redirect('/')

@app.route('/reset', methods=['GET'])
def reset_game():
	session.clear()
	return redirect('/')

app.run(debug=True, port=8585)