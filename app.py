from flask import Flask, render_template, Response, request
import threading
from work_db import *

app = Flask(__name__)
frame_r = 0
stat = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def render():
    dbwork = DBWork('lessons.db')
    schedule = dbwork.select_all('lessons', Schedule)
    schedule.sort(key=lambda x: (x[1], x[2]))
    return render_template('tables.html', schedule=schedule)
@app.route ('/result')
def result():
    global stat 
    stat = int(request.args.get('stat'))
    print(stat)
    return '', 200, {'Content-Type': 'text/plain'}
    

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
