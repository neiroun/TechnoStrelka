from flask import Flask, render_template, Response, request
import threading
from work_db import *

app = Flask(__name__)
frame_r = 0
stat = '0'

@app.route('/')
def index():
    return render_template('index.html') #comment to delete

@app.route('/table')
def render():
    global stat
    dbwork = DBWork('lessons.db')
    schedule = dbwork.select_all('lessons', Schedule)
    schedule.sort(key=lambda x: (x[1], x[2]))
    return render_template('tables.html', schedule=schedule, stat=stat)

@app.route ('/result')
def result():
    global stat 
    stat = str(request.args.get('stat'))
    print(stat)
    return '', 200, {'Content-Type': 'text/plain'}

@app.route('/reset')
def reset():
    return render_template('reset.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
