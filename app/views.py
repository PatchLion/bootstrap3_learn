#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'PatchLion'

from flask import Flask, send_file

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return "Bootstrap3 test"

@app.route("/<html>")
def html(html):
    return send_file("templates/"+html)