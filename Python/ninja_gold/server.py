from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key="secretsauce81"

@app.route('/')
def index():
	return render_template('index.html')


app.run(debug=True, port=8585)