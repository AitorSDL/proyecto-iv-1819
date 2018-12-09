from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def index():
  
    phrase = {"status" : "OK"}
    return jsonify(phrase)

@app.route("/status")
def check():
  
  with open('status.json') as f:
    data = json.load(f)
    
  response = app.response_class(
    response=json.dumps(data),
    status=200,
    mimetype='application/json'
  )
  
  return response
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
