import tkinter as tk
import tkinter.messagebox as mb
from quain_func import *
from save_result import *

class MainWindow():
    def main_window(self,root):

        func = Quain()
        save = ResultSaver()

        def hide():
            m_window.withdraw()
            root.deiconify()

        def add_vars(line):
            new_line = line
            if not nx.get():
                new_line += " + (x"
            else:
                new_line += " + (\u00ACx"

            if not ny.get():
                new_line += " \u00B7 y "
            else:
                new_line += " \u00B7 \u00ACy"

            if not nz.get():
                new_line += " \u00B7 z)"
            else:
                new_line += " \u00B7 \u00ACz)"
            return new_line.strip().strip("+")

        def add():
            lbl_origl.config(text = add_vars(lbl_origl.cget("text")))

        def qcall():
            result = save.save(lbl_origl.cget("text"))
            if(result):
                lbl_solve.config(text = result)
            else:
                lbl_solve.config(text=func.solving(lbl_origl.cget("text")))



        def clear():
            lbl_origl.config(text="")

        def help():
            mb.showinfo("Помощь","Для ввода уравнения необходимо выбрать переменные, которые являются отрицательными "
                                 "и поставить над ними галочку, после чего нажать '+', после ввода уравнения"
                                 " нужно нажать кнопку 'Минимизировать'.")



        root.withdraw()

        m_window = tk.Toplevel()

        m_window.title("Окно программы")

        m_window.geometry("600x320")
        m_window.resizable(width=False, height=False)

        main_frame = tk.Frame(master=m_window,bg="grey")
        main_frame.pack(fill=tk.BOTH,expand=True)

        nx = tk.BooleanVar()
        cbtn_x = tk.Checkbutton(main_frame,variable=nx)
        cbtn_x.place(x=10, y=50)

        lbl_x = tk.Label(main_frame,text="x",bg="grey",font=60)
        lbl_x.place(x=15,y=80)

        ny = tk.BooleanVar()
        cbtn_y = tk.Checkbutton(main_frame, variable=ny)
        cbtn_y.place(x=40, y=50)

        lbl_y = tk.Label(main_frame, text="\u00B7  y", bg="grey", font=60)
        lbl_y.place(x=30, y=80)

        nz = tk.BooleanVar()
        cbtn_z = tk.Checkbutton(main_frame, variable=nz)
        cbtn_z.place(x=70, y=50)

        lbl_z = tk.Label(main_frame, text="\u00B7  z", bg="grey", font=60)
        lbl_z.place(x=58, y=80)


        btn_add = tk.Button(main_frame,text="+",width=3,height=1,command=add)
        btn_add.place(x=100,y=80)

        btn_ex = tk.Button(main_frame,text="Выйти",command=hide,width=10,height=1)
        btn_ex.place(x=520, y=1)

        lbl_origl = tk.Label(main_frame,text="",bg="grey",font = 80)
        lbl_origl.place(x=20,y=120)


        btn_solve = tk.Button(main_frame,text="Минимизировать",command=qcall)
        btn_solve.place(x=490,y=180)

        lbl_solve = tk.Label(main_frame,text="---------------",bg="grey",font = 80)
        lbl_solve.place(x=20,y=230)

        lbl_variables = tk.Label(main_frame,text = "Ввод уравнения:",bg="grey",font=100)
        lbl_variables.place(x=10,y=10)

        lbl_result = tk.Label(main_frame, text="Минимизированное уравнение:", bg="grey", font=100)
        lbl_result.place(x=10, y=180)

        btn_clr = tk.Button(main_frame,text="Очистить",command=clear)
        btn_clr.place(y=100,x=500)

        btn_hlp = tk.Button(main_frame,text="Помощь",command=help)
        btn_hlp.place (y = 1,x = 400)