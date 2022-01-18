#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("test.html", message = "Bienvenue")

if __name__ == "__main__":
    app.run()