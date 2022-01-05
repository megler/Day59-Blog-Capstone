# blogCapstone.py
#
# Python Bootcamp Day 59 - Flask Blog Capstone
# Usage:
#      A more robust blog using Flask and JSON data. Day 59 Python Bootcamp.
#
# Marceia Egler January 5, 2022

import json
from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    data_endpoint = "https://api.npoint.io/518f1f99a0306ee5ceea"
    r = requests.get(data_endpoint)
    all_posts = r.json()
    return render_template("index.html", blog_posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<id>")
def blog(id):
    data_endpoint = "https://api.npoint.io/518f1f99a0306ee5ceea"
    r = requests.get(data_endpoint)
    all_posts = r.json()
    id = int(id) - 1
    title = all_posts[id]["title"]
    body = all_posts[id]["body"]
    subtitle = all_posts[id]["subtitle"]
    return render_template(
        "post.html", title=title, body=body, subtitle=subtitle
    )


if __name__ == "__main__":
    app.run(debug=True)
