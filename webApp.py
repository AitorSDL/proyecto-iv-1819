from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def check():
  
  with open('status.json') as f:
    data = json.load(f)
    
  response = app.response_class(
    response=json.dumps(data),
    status=200,
    mimetype='application/json'
  )
  
  return response

  
@app.route("/todo")
def index():
  return "TEST"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
