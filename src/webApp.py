from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def index():
  
  with open('status.json') as f:
    response = json.load(f)
    
  response = app.response_class(
    response=json.dumps(data),
    status=200,
    mimetype='application/json'
  )
  
  return response

@app.route("/todo")
def check():
  return "TEST"
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
