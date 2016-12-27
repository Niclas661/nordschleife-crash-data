from flask import Flask, render_template, request, jsonify
import os, glob, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/section/<sectionName>')
def get_section(sectionName):
    content_file = open('wiki/sections.json', 'r')
    content_str = content_file.read()
    json_data = json.loads(content_str)
    return render_template('section.html', name=sectionName, description=json_data['sections'][sectionName], video=json_data['videos'][sectionName])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
