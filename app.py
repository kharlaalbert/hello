from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route('/')
def hello():
	#return 'Hello World!'
	return render_template('helloworld.html')
	
if __name__ == '__main__':
    app.run()