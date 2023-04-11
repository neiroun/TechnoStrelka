import sqlite3
#from app import stat

class DBWork:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_items = {}

    def select_all(self, table, class_type, group_name):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        result = cur.execute(f'SELECT * FROM {table} WHERE group_name="{group_name}"'
                             ).fetchall()
        con.close()
        return class_type.pack(result)

    def create_table(self, table):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'CREATE TABLE IF NOT EXISTS {table} ('
        for col_name, col_type in self.db_items.items():
            sql_query += f'{col_name} {col_type}, '
        sql_query = sql_query[:-2]
        sql_query += f')'
        cur.execute(sql_query)
        con.close()

    def select_groups(self, table):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        result = cur.execute(f'SELECT DISTINCT group_name FROM {table} '
                             ).fetchall()
        result = [x[0] for x in result]
        con.close()
        return result

    def insert(self, table, entity_args):
        # assert len(entity_args) == len(self.db_items.keys()) - (1 if 'id' in self.db_items.keys() else 0)
        if1 = len(self.db_items.keys()) - (1 if 'id' in self.db_items.keys() else 0)
        if2 = len(entity_args)
        if len(entity_args) != len(self.db_items.keys()) - (1 if 'id' in self.db_items.keys() else 0):
            return
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'INSERT INTO {table} ('
        for arg in self.db_items.keys():
            if arg == 'id':
                continue
            sql_query += f'{arg}, '
        sql_query = sql_query[:-2] + f') VALUES ('
        for arg in entity_args:
            sql_query += f'?, '
        sql_query = sql_query[:-2]
        sql_query += f')'
        cur.execute(sql_query, entity_args)
        con.commit()
        con.close()

    def delete_by_id(self, table, id):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'DELETE FROM {table} WHERE id = {id}'
        cur.execute(sql_query)
        con.commit()
        con.close()

    def delete_by_group(self, table, group_name):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'DELETE FROM {table} WHERE group_name = "{group_name}"'
        cur.execute(sql_query)
        con.commit()
        con.close()

    def delete_by_timedate(self, table, time, day, group_name):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'DELETE FROM {table} WHERE day = {day} AND time = {time} AND group_name = "{group_name}"'
        cur.execute(sql_query)
        con.commit()
        con.close()

    def update_by_timedate(self, table, schedule):
        assert isinstance(schedule, Schedule)
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'UPDATE {table} SET ' \
                    f'room={schedule.room}, teacher={schedule.teacher}, ' \
                    f'subject={schedule.subject} ' \
                    f'WHERE day = {schedule.day} AND time = {schedule.time} AND group_name={schedule.group_name}'
        cur.execute(sql_query)
        con.commit()
        con.close()

    def update_the_whole_group(self, table, group_name, schedule_list):
        self.delete_by_group(table, group_name)
        for item in schedule_list:
            self.insert(table, item)



class Schedule:
    @staticmethod
    def get_description():
        description = {
            'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'time': 'INT',
            'day': 'INT',
            'room': 'TEXT',
            'teacher': 'TEXT',
            'group_name': 'TEXT',
            'subject': 'TEXT'
        }
        return description
    def __init__(self, time, day, room, teacher, group_name, subject):
        self.time = time
        self.day = day
        self.room = room
        self.teacher = teacher
        self.group_name = group_name
        self.subject = subject

    @staticmethod
    def pack(schedule):
        result = [['' for i in range(4)] for j in range(5)]
        print(schedule)
        for entity in schedule:
            print(result)
            result[entity[2]][entity[1]] = f'{entity[3]}, {entity[6]}, {entity[4]}'
        return result

#db_work = DBWork("lessons.db")
#db_work.db_items = {
    # 'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
    # 'time': 'INT',
    # 'day': 'INT',
    # 'room': 'TEXT',
    # 'teacher': 'TEXT',
    # 'group_name': 'TEXT',
    # 'subject': 'TEXT'
#}
#db_work.create_table('lessons')
# db_work.db_items = {
#     'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
#     'FIO': 'INT',
#     'hour_per_week': 'INT'
# }
# db_work.create_table('teachers')
#db_work.insert('lessons', [0, 0, '"101"', '"Иванов И.И"', '"1П"', '"Python"'])
#db_work.insert('lessons', [2, 3, '"102"', '"Иванов И.И"', '"2P"', '"Java"'])
# db_work.delete_by_id('lessons', 2)
#print(db_work.select_all('lessons', Schedule, stat))
#print(db_work.select_groups('lessons'))

