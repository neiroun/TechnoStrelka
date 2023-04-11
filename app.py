from flask import Flask, render_template, Response, request
import threading
from work_db import *
import csv

app = Flask(__name__)
frame_r = 0
stat = '0'
group = ''
id = ''
teachers = list()
schedule = None

with open('static/teach.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";", quotechar='"')
    teachers = list(reader)[1:]

@app.route('/')
def index():
    return render_template('index.html') #comment to delete

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/del')
def delet():
    global id, schedule, stat, teachers 
    id = int(request.args.get('id'))
    with open('static/teach.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                user_info = list(reader)[1:]
                print(user_info)

    if id <= len(user_info):
        cnt = 1
        for i in user_info:
            if int(i[0]) == id:
                del user_info[user_info.index(i)]
                print('ok')
                print(user_info)
        for i in user_info:
            i[0] = str(cnt)
            cnt += 1
        file.close()
    with open('static/teach.csv', 'w', encoding='utf-8') as file:
                    file.write(f'"id";"ФИО";"Предмет";\n')
                    for i in user_info:
                        if i != user_info[-1]:
                            file.write(f'"{i[0]}";"{i[1]}";"{i[2]}"\n')
                        else:
                            file.write(
                                f'"{i[0]}";"{i[1]}";"{i[2]}"')
                    file.close()
    with open('static/teach.csv', 'r', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";", quotechar='"')
        teachers = list(reader)[1:]
    return render_template('tables.html', schedule=schedule, stat=stat, teachers=teachers, val=len(teachers))

@app.route('/add')
def add():
    global id, schedule, stat, teachers 
    FIO = str(request.args.get('FIO'))
    object = str(request.args.get('obj'))
    with open('static/teach.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                user_info = list(reader)[1:]
    with open('static/teach.csv', 'a', encoding='utf-8') as file:
            file.write(f'\n"{int(user_info[-1][0]) + 1}";"{FIO}";"{object}"')
    with open('static/teach.csv', 'r', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";", quotechar='"')
        teachers = list(reader)[1:]
    return render_template('tables.html', schedule=schedule, stat=stat, teachers=teachers, val=len(teachers))


@app.route('/table', methods=['GET', 'POST'])
def render():
    global stat, teachers, schedule
    print(stat)
    dbwork = DBWork('lessons.db')
    dbwork.db_items = Schedule.get_description()
    schedule = dbwork.select_all('lessons', Schedule, stat)
    schedule.sort(key=lambda x: (x[1], x[2]))
    return render_template('tables.html', schedule=schedule, stat=stat, teachers=teachers, val=len(teachers))

@app.route ('/result')
def result():
    global stat 
    stat = str(request.args.get('stat'))
    print('STAT: ', stat)
    return '', 200, {'Content-Type': 'text/plain'}

# @app.route('/reset', methods=['GET', 'POST'])
# def reset():
#     if request.method == 'POST':
#         global stat
#         dbwork = DBWork('lessons.db')
#         schedule = dbwork.select_all('lessons', Schedule, stat)
#         schedule.sort(key=lambda x: (x[1], x[2]))
#         return render_template('tables.html', schedule=schedule, stat=stat)
#     return render_template('timetable.html')

@app.route('/reset', methods=['GET', 'POST'])
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
                    result_list.append([j, i, info[0], info[1], stat, info[2]])
        print(result_list)
        print('********************')
        dbwork = DBWork('lessons.db')
        dbwork.db_items = Schedule.get_description()
        dbwork.update_the_whole_group('lessons', stat, result_list)
        print(schedule_list)
        return render_template('timetable.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
