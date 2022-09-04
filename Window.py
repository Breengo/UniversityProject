import tkinter as tk
import tkinter.messagebox as mb
from RegistrationWindow import *
from main_window import *
import sqlite3



class AuthorizationWindow():
    def open_window_r(self):
        swindow = SignUpWindow()
        swindow.openRegWindow(root)

    def open_window_m(self):
        mwindow = MainWindow()
        mwindow.main_window(root)

    def sign_in(self):
        password = ent_pass.get()
        login = ent_login.get()
        cur.execute('SELECT * FROM users WHERE login == ? AND password == ?',(login,password))
        result = cur.fetchone()
        if result != None:
            window.open_window_m()
        else:
            mb.showerror("Ошибка","Неправильный логин или пароль")

window = AuthorizationWindow()

root = tk.Tk()
root.title("Окно авторизации")
root.geometry("400x250")
root.resizable(width=False,height=False)

frame1 = tk.Frame(bg="grey")
frame1.pack(fill=tk.BOTH, expand=True)


lbl_greeting = tk.Label(frame1,text= "Авторизация",bg="grey",font=60)
lbl_greeting.place(x=150,y=10)


btn_sign = tk.Button(frame1,height=1,width=15, bg="white",text="Войти",relief=tk.RAISED,command=window.sign_in)
btn_sign.place(x=150,y = 185)

lbl_login = tk.Label(frame1,text = "Логин",bg="grey",width=15,height=1,font=30)
ent_login = tk.Entry(frame1,width=25)
lbl_login.place(x = 15,y = 60)
ent_login.place(x=120,y=65)


lbl_pass = tk.Label(frame1,text = "Пароль",bg="grey",width=15,height=1,font=30)
ent_pass = tk.Entry(frame1,width=25)
lbl_pass.place(x=15,y=120)
ent_pass.place(x=120,y=125)


btn_reg = tk.Button(frame1,text="Регистрация",command = window.open_window_r)
btn_reg.place(x=320,y=225)


conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
            login TEXT,
            password TEXT);""")
conn.commit()

root.mainloop()