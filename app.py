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
    return '', 200, {'Content-Type': 'text/plain'}

@app.route('/reset')
def reset():
    return render_template('reset.html')

@app.route('/timetable', methods=['GET', 'POST'])
def timetable():
    if request.method == 'GET':
        print('GET')
        return render_template('timetable.html')
    elif request.method == 'POST':
        print('POST')
        schedule_list = []
        for i in range(5):
            schedule_row = []
            for j in range(4):
                schedule_row.append(str(request.form['in'+str(i+1)+str(j+1)]))
            schedule_list.append(schedule_row)
        #ПРИНИМАЕТСЯ СОДЕРЖИМОЕ ИНПУТОВ, КОТОРОЕ НУЖНО РАЗБИТЬ НА СПИСКИ И ЗАКИНУТЬ В update_the_whole_group
        #schedule_list нужно привести к виду, чтобы он содержал элементы одного пункта расписания
        dbwork = DBWork('lessons.db')
        dbwork.update_the_whole_group('lessons', '1П', schedule_list)
        print(schedule_list)
        return render_template('timetable.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
