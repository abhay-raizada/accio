from flask import Flask
import csv
import os
import json
app = Flask(__name__)

@app.route("/resource")
def resource():
    return "Resource!"