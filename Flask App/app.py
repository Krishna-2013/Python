from flask import Flask, redirect, request, url_for, session, Response

app = Flask(__name__)

#homepage login page
@app.route("/", methods=["GET", "POST"])
def login():
    