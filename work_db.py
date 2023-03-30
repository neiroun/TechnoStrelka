import sqlite3


class DBWork:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_items = {}

    def select(self, table):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        result = cur.execute(f'SELECT * FROM {table}'
                             ).fetchall()
        con.close()
        return result

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


db_work = DBWork("lessons.db")
db_work.create_table('lessons')
db_work.db_items = {
    'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
    'time': 'INT',
    'day': 'INT',
    'room': 'TEXT',
    'teacher': 'TEXT',
    'group': 'TEXT',
    'subject': 'TEXT'
}
db_work.create_table('teachers')
db_work.db_items = {
    'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
    'FIO': 'INT',
    'hour_per_week': 'INT'
}
db_work.insert('lessons', [1, 1, '"101"', '"Иванов И.И"'])
#db_work.insert('lessons', [1, 1, '"room1"', '"me"'])
#db_work.delete_by_id('lessons', 2)
#print(db_work.select('lessons'))
