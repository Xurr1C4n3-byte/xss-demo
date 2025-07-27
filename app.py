from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "Go to /index.html"

@app.route('/index.html')
def serve_index():
    return send_file('index.html')
