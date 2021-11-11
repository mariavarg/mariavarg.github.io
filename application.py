<!DOCTYPE html>

import os
from cs50 import SQL
from flask import Flask, redirect, render_template,request

db = SQL("sqlite:///homepage.db)

<meta name="viewport" content="width=device-width-10, initial-scale=1.0">
<html lang="en">
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
        <link href="styles.css" rel="stylesheet">
        <title>My Webpage</title>
    </head>
<head>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">
<style>
body, h1 {
  font-family: "Sofia", sans-serif;
}
</style>
</head>

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

def register():
    if not request.form.get("email") or request.form.get("Steppenwolf") not in STEPPENWOLF:
        return render_template("error.html")

    return render_template("success.html")

<tbody>{% for voter in voters %}
    <tr>
        <td>{{ voter.name}}</td>
        <td>{{ voter.Steppenwolf }}</td>
            <form action="/deregister" method="post">
                <input name="id" type="hidden" value="{{ voter.id }}"
                <input type="submit" value="Deregister">
            </form>
    </tr>

    {% endfor %}
    </tbody>

def register():
    if not email:
        return render_template("error.html", message="Missing email")
        Steppenwolf = request.form.get("Steppenwolf")
    if Steppenwolf not in STEPPENWOLF:
        return render_template("error.html", message="Invalid vote")

        db.execute("INSERT INTO voters (name, Steppenwolf) VALUES(?, ?)", name, Steppenwolf

        message = Message("Your vote has been validated", recipients=[email])
        mail.send(message)

    return redirect("/voters")

def voters():
    voters = db.execute("SELECT * FROM voters")
    return render_template("voters.html", voters=voters)
                   
BACKUP DATABASE voters;
TO DISK = 'D:\BACKUP DATABASE- mariav.art\votersDB.bak';                   


