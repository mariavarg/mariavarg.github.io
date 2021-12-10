from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return rendrer_template"index.html"

export FLASK_APP=application.py
export FLASK_DEBUG=1
flask run

@app.route("/login", methods=['GET', 'POST'])
def login():
  if not request.form.get("username")
    return apology("must provide username")
  
  if request method== "POST":
    return render_template"Success.html"
  else
    return render_template"Failure.html"
  
  
