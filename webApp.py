from flask import Flask, json

@app.route("/")
def check():
  response = 0
  with open('status.json') as f:
    response = json.load(f)
  return response

  
@app.route("/todo")
def index():
  return "TEST"
