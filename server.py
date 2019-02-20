from flask import Flask
import csv
import os
import json
app = Flask(__name__)

@app.route("/<file_path>")
def index(file_path):
    with open(file_path + '.csv', mode = 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        result = {}
        for row in csv_reader:
            if line_count == 0:
                for header in row.keys():
                    result[header] = []
                line_count += 1
        for header in result.keys():
            result[header].append(row[header])
        line_count += 1
        if line_count > 10:
            returnjson.dumps(result)
    return json.dumps(result)