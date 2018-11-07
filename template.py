from flask import Flask, render_template, request
from flask_bootstrap  import Bootstrap


app = Flask(__name__)


bootstrap = Bootstrap(app)

@app.route('/')
def index():

	comments = [
		{
			'username' : 'zero',
			'comment' : 'hello flask '
		},
		{
			'username': 'dancesmile',
			'comment': ' falsk template '
		},
		{
			'username': 'butterfly',
			'comment': ' the free'
		}
	]

	return render_template('index.html', request = request, comments = comments)

@app.route('/user')
def user():
	return render_template('user.html')


@app.errorhandler(404)
def page_404(e):
	return render_template('404.html')
if __name__ == '__main__': 

	app.run(debug=True)