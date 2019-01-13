from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def index():
  
  with open('seller.json') as f:
    data = json.load(f)
  
  return data


@app.route("/status")
def check():
  
  with open('status.json') as f:
    data = json.load(f)
  
  return data

@app.route("/random")
def randomItem():
    
    return "TODO"  
  
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
