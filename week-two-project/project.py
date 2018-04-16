from flask import flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
	return "Hello World"

if __name__ == '__main__':
	app.run(debug = True)