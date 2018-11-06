from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def check():
  response = 0
  with open('status.json') as f:
    response = json.load(f)
  return response

  
@app.route("/todo")
def index():
  return "TEST"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
