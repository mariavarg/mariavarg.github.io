from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return rendrer_template"index.html"

export FLASK_APP=application.py
export FLASK_DEBUG=1
flask run
