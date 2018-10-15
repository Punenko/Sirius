#task 1
from math import sqrt
from tkinter import *
from tkinter import messagebox

def display_answer():
    a, b, c = float(A.get()), float(B.get()), float(C.get())

    D = b ** 2 - 4 * a * c
    if a==0 and b==0 and c==0:
        messagebox.showinfo("Ответ", "Любое число походит")
    elif D<0 or (a==0 and b==0 and c!=0):
        messagebox.showinfo("Ответ", "Нет решений")
    elif D == 0:
        x1 = (b * (-1)) / (2 * a)
        messagebox.showinfo("Ответ", "X1=" + str(x1))
    else:
        x1 = ((-1) * b - sqrt(D)) / (2 * a)
        x2 = ((-1) * b + sqrt(D)) / (2 * a)
        messagebox.showinfo("Ответ","X1=" + str(x1) +"  " +"X2=" + str(x2))

root = Tk()
root.title("Решение Уравнения")
root.geometry("270x130")

A=StringVar()
B=StringVar()
C=StringVar()

a_label=Label(text="Введите а:")
b_label=Label(text="Введите b:")
c_label=Label(text="Введите c:")

a_label.grid(row=0, column=0)
b_label.grid(row=1, column=0)
c_label.grid(row=2, column=0)

a_e=Entry(textvariable=A)
b_e=Entry(textvariable=B)
c_e=Entry(textvariable=C)

a_e.insert(0,'0')
b_e.insert(0,'0')
c_e.insert(0,'0')

a_e.grid(row=0,column=1)
b_e.grid(row=1,column=1)
c_e.grid(row=2,column=1)

calc=Button(text="Рассчитать",command=display_answer)
calc.grid(row=3,column=1)


root.mainloop()



