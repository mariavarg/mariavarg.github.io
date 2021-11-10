from cs50 import SQl
from flask import Flask, redirect, render_template, request, session, jsonify

def register():
    if not request.form.get("name") or request.form.get("Steppenwolf") not in STEPPENWOLF
        return render_template("Please fill out the fields")

    return render_template("Your choice has been validated")

app = Flask(__name__)
VOTERS ={}

STEPPENWOLF= [
    "Democrats",
    "Rebublicans",
    "Other"
    ]

def mainpage():
    email = request.form.get("email")
    return render_template("mainpage.html", Steppenwolf=STEPPENWOLF)

def register():
    if not name:
        return render_template("error.html", message="Missing name")
        Steppenwolf = request.form.get("Steppenwolf")
    if Steppenwolf not in STEPPENWOLF:
        return render_template("error.html", message="Invalid vote")

        db.execute("INSERT INTO voters (name, Steppenwolf) VALUES(?, ?)", name, Steppenwolf

    VOTERS[name] = Steppenwolf
    return redirect("/voters")

def voters():
    voters = db.execute("SELECT * FROM voters")
    return render_template("voters.html", voters=voters)



