from flask import Flask, render_template, Response, request
import threading
from work_db import *
import csv

app = Flask(__name__)
frame_r = 0
stat = '0'
group = ''
teachers = list()

with open('static/teach.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";", quotechar='"')
    teachers = list(reader)[1:]

@app.route('/')
def index():
    return render_template('index.html') #comment to delete

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/table', methods=['GET', 'POST'])
def render():
    global stat
    dbwork = DBWork('lessons.db')
    schedule = dbwork.select_all('lessons', Schedule)
    schedule.sort(key=lambda x: (x[1], x[2]))
    return render_template('tables.html', schedule=schedule, stat=stat, teachers=teachers, val=len(teachers))

@app.route ('/result')
def result():
    global stat 
    stat = str(request.args.get('stat'))
    print(stat)
    return '', 200, {'Content-Type': 'text/plain'}

@app.route('/reset')
def reset():
    return render_template('timetable.html')

@app.route('/timetable', methods=['GET', 'POST'])
def timetable():
    global group
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
        #group = str(request.form["group_selector"])
        #ПРИНИМАЕТСЯ СОДЕРЖИМОЕ ИНПУТОВ, КОТОРОЕ НУЖНО РАЗБИТЬ НА СПИСКИ И ЗАКИНУТЬ В update_the_whole_group
        #schedule_list нужно привести к виду, чтобы он содержал элементы одного пункта расписания
        # 'room, teacher, subject'
        result_list = []
        for i in range(5):
            for j in range(4):
                info = schedule_list[i][j].split(',')
                if len(info) == 3:
                    print(info)
                    result_list.append(Schedule(j, i, info[0], info[1], group, info[2]))
        print(result_list)
        print('********************')
        dbwork = DBWork('lessons.db')
        dbwork.update_the_whole_group('lessons', group, schedule_list)
        print(schedule_list)
        return render_template('timetable.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
