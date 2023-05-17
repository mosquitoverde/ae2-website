#imported flask
from flask import Flask

#created flask app
app = Flask(__name__)

#register route to application
@app.route("/")
def hello_world():
  return "Hello, World"

#if it is running on
if __name__ == "__main__":
  #start app
  app.run(host="0.0.0.0", debug=True)