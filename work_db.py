import sqlite3


class DBWork:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_items = {}

    def db_work(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        result = cur.execute('"SELECT * FROM {self.db_name}'
                             'WHERE year = 2010"').fetchall()
        con.close()
        return result

    def create_db(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql_query = f'CREATE TABLE {self.db_name} ('
        for col_name, col_type in self.db_items.items():
            sql_query += f'{col_name} {col_type}, '
        sql_query = sql_query[:-2]
        sql_query += f')'
        cur.execute(sql_query)


db_work = DBWork("lessons.db")
db_work.db_items = {
    'time': 'INT',
    'day': 'INT',
    'room': 'STRING',
    'teacher': 'STRING'
}
db_work.create_db()
