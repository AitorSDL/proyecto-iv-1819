from flask import Flask, json

@app.route("/")
def check():
  
  with open('status.json') as f:
    response = json.load(f)
    
  response = app.response_class(
    response=json.dumps(data),
    status=200,
    mimetype='application/json'
  )
  
  return response

  
@app.route("/todo")
def index():
  return "TEST"
