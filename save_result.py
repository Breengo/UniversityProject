from quain_func import *
import sqlite3
import tkinter.messagebox as mb


class ResultSaver():
    def save(self,line):
        conn = sqlite3.connect('results.db')
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS results(
                    func TEXT,
                    result TEXT);""")
        conn.commit()

        funct = line
        function = Quain()

        cur.execute('SELECT * FROM results WHERE func == ?', (funct,))
        result = cur.fetchone()
        if result == None:
            cur.execute("""INSERT INTO results(func,result)
                                        VALUES(?,?);""", (funct,function.solving(funct)))
            conn.commit()
            return False
        else:
            mb.showinfo("Информация", "Данная функция уже есть в БД")
            return result[1]
