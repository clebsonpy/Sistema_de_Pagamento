import sqlite3

class Connect():

    def __init__(self, nome_db):
        try:
            self.conn = sqlite3.connect('%s.db' % nome_db)
            self.cursor = self.conn.cursor()
            print("Banco: %s " % nome_db)

        except sqlite3.Error:
            print("Erro")

    def close_db(self):
        if self.conn:
            self.conn.close()
            print('Banco Fechado')

    def commit_db(self):
        if self.conn:
            self.conn.commit()
            print('Dado Gravado')