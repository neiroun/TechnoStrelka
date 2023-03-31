import sqlite3


class DBWork:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_items = {}

    def select_all(self, table, class_type):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        result = cur.execute(f'SELECT * FROM {table}'
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
        assert len(entity_args) == len(self.db_items.keys()) - (1 if 'id' in self.db_items.keys() else 0)
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'INSERT INTO {table} ('
        for arg in self.db_items.keys():
            if arg == 'id':
                continue
            sql_query += f'{arg}, '
        sql_query = sql_query[:-2] + f') VALUES ('
        for arg in entity_args:
            sql_query += f'{arg}, '
        sql_query = sql_query[:-2]
        sql_query += f')'
        cur.execute(sql_query)
        con.commit()
        con.close()

    def delete_by_id(self, table, id):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'DELETE FROM {table} WHERE id = {id}'
        cur.execute(sql_query)
        con.commit()
        con.close()

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
        for entity in schedule:
            result[entity[1]][entity[2]] = f'{entity[3]}, {entity[6]}, {entity[4]}'
        return result

db_work = DBWork("lessons.db")
db_work.db_items = {
    'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
    'time': 'INT',
    'day': 'INT',
    'room': 'TEXT',
    'teacher': 'TEXT',
    'group_name': 'TEXT',
    'subject': 'TEXT'
}
db_work.create_table('lessons')
# db_work.db_items = {
#     'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
#     'FIO': 'INT',
#     'hour_per_week': 'INT'
# }
# db_work.create_table('teachers')
#db_work.insert('lessons', [0, 0, '"101"', '"Иванов И.И"', '"1P"', '"Python"'])
#db_work.insert('lessons', [2, 3, '"102"', '"Иванов И.И"', '"2P"', '"Java"'])
# db_work.delete_by_id('lessons', 2)
print(db_work.select_all('lessons', Schedule))
print(db_work.select_groups('lessons'))
