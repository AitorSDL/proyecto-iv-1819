from flask import Flask


app = Flask(__name__)


@app.route('/')

def hello_world():
	return """<!doctype html>
<html>
  <head>
	<link rel="stylesheet" type="text/css href="styles.css"/>
	<title>Título genérico</title>
  </head>
  <body>
	<h1>Hello, World!</h1>
	<ul>Lista
	<li>Número 1</li>
	<li>Número 2</li>
	</ul>
	<img src="static/imagen.jpg">
  </body>
</html>"""

@app.route('/user/pepe')

def pepe():
	return "Test"

@app.errorhandler(404)

def error404(e):
	return """<!doctype html>
<html>
  <head>
	<title>Page not found</title>
  </head>
  <body>
        <h1>We need to go back!</h1>
  </body>
</html>"""	


if __name__ == '__main__':

	app.run(host='0.0.0.0', debug=True)
