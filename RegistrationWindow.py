import tkinter as tk
import sqlite3
import tkinter.messagebox as mb

class SignUpWindow():
    def openRegWindow(self,root):

        def hide():
            rWindow.withdraw()
            root.deiconify()

        def registration():
            log = ent_rlogin.get()
            passw = ent_rpass.get()

            if len(log)<3 or " " in log:
                mb.showerror("Ошибка","Некорректный логин")
                return
            elif len(passw) < 5 or " " in passw:
                mb.showerror("Ошибка","Некорректный пароль")
                return

            user = (log,passw)

            conn = sqlite3.connect('users.db')
            cur = conn.cursor()

            cur.execute('SELECT * FROM users WHERE login == ?', (log,))
            result = cur.fetchone()
            if result == None:
                cur.execute("""INSERT INTO users(login,password)
                            VALUES(?,?);""", user)
                conn.commit()
                mb.showinfo("Успех","Аккаунт создан")
            else:
                mb.showerror("Ошибка", "Логин занят")

            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                login TEXT,
                password TEXT);""")
            conn.commit()


        root.withdraw()

        rWindow = tk.Toplevel()

        rWindow.title("Окно регистрации")
        rWindow.geometry("400x250")
        rWindow.resizable(width=False, height=False)

        frame2 = tk.Frame(bg="grey",master=rWindow)
        frame2.pack(fill=tk.BOTH, expand=True)

        lbl_rgreeting = tk.Label(frame2, text="Регистрация", bg="grey", font=60)
        lbl_rgreeting.place(x=150, y=10)

        btn_reg = tk.Button(frame2, height=1, width=15, bg="white", text="Создать", relief=tk.RAISED,command=registration)
        btn_reg.place(x=150, y=185)

        lbl_rlogin = tk.Label(frame2, text="Логин", bg="grey", width=15, height=1, font=30)
        ent_rlogin = tk.Entry(frame2, width=25)
        lbl_rlogin.place(x=15, y=60)
        ent_rlogin.place(x=120, y=65)

        lbl_rpass = tk.Label(frame2, text="Пароль", bg="grey", width=15, height=1, font=30)
        ent_rpass = tk.Entry(frame2, width=25)
        lbl_rpass.place(x=15, y=120)
        ent_rpass.place(x=120, y=125)

        btn_au = tk.Button(frame2, text="Окно авторизации",command=hide)
        btn_au.place(x=290, y=225)
