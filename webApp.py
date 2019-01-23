from flask import Flask, json, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  with open('seller.json') as f:
    data = json.load(f)
  
  response = app.response_class(
    response=json.dumps(data),
    status=200,
    mimetype='application/json'
  )
  
  return response


@app.route("/status")
def check():
  
  return jsonify(status='OK')
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
