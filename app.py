from flask import Flask, render_template, Response, request
import threading

app = Flask(__name__)
frame_r = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def render():
    return render_template('main.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
    