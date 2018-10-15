from tkinter import *
a=1
root = Tk()
root.title("Расписание")
root.geometry("800x600")
waste=[]
Name=[]
Start=[]
Ending=[]
Time1=[]
Time2=[]
H1,H2,M1,M2,D1,D2,MO1,MO2,Y1,Y2=[],[],[],[],[],[],[],[],[],[]

def add_something():
    Name.append(A.get())
    Start.append(B.get())
    Ending.append(C.get())
    for i in range(len(Name)):
        Start[i] = Start[i].replace('.', '').replace('-', '').replace(',', '')
        Ending[i] = Ending[i].replace('.', '').replace('-', '').replace(',', '')

    a_e.delete(0,END)
    b_e.delete(0,END)
    c_e.delete(0,END)

def vivod():
    for i in range(len(Name)):
        H1.append(Start[i][0]+Start[i][1])
        H2.append(Ending[i][0]+Ending[i][1])
        M1.append(Start[i][2] + Start[i][3])
        M2.append(Ending[i][2]+Ending[i][3])
        D1.append(Start[i][4] + Start[i][5])
        D2.append(Ending[i][4] + Ending[i][5])
        MO1.append(Start[i][6] + Start[i][7])
        MO2.append(Ending[i][6] + Ending[i][7])
        Y1.append(Start[i][8] + Start[i][9]+Start[i][10]+Start[i][11])
        Y2.append(Ending[i][8] + Ending[i][9]+ Ending[i][10]+ Ending[i][11])
        Time1.append(int(H1[i])*60+int(M1[i])+int(D1[i])*1440+int(MO1[i])*43200+int(Y1[i])*518400)
        Time2.append(int(H2[i])*60+int(M2[i])+int(D2[i])*1440+int(MO2[i])*43200+int(Y2[i])*518400)
    t=Time1.index(min(Time1))
    a=str(str(Name[t])+'  c '+str(H1[t])+' : '+str(M1[t])+'  '+str(D1[t])+'.'+str(MO1[t])+'.'+str(Y1[t])+
            '  до  '+str(H2[t])+' : '+str(M2[t])+'  '+str(D2[t])+'.'+str(MO2[t])+'.'+str(Y2[t]))
    text.insert(END,'\n'+a)
    for i in range(len(Name)-1):
        t=Time1.index(min(Time1))
        m=Time2[t]
        Time1.remove(min(Time1))
        Name.remove(Name[t])
        Time2.remove(Time2[t])
        H1.remove(H1[t])
        M1.remove(M1[t])
        D1.remove(D1[t])
        MO1.remove(MO1[t])
        Y1.remove(Y1[t])
        H2.remove(H2[t])
        M2.remove(M2[t])
        D2.remove(D2[t])
        MO2.remove(MO2[t])
        Y2.remove(Y2[t])
        if int(m)<=int(min(Time1)):
            T=Time1.index(min(Time1))
            a = str(str(Name[T]) + '  c ' + str(H1[T]) + ' : ' + str(M1[T]) + '  ' + str(D1[T]) + '.' + str(MO1[T]) + '.' + str(Y1[T]) +
                    '  до  ' + str(H2[T]) + ' : ' + str(M2[T]) + '  ' + str(D2[T]) + '.' + str(MO2[T]) + '.' + str(Y2[T]))
            text.insert(END,'\n'+a)
        else:
            waste.append(str(Name[Time1.index(min(Time1))]))
    for i in range(len(waste)):
        text.insert(END,'\n'+waste[i]+'   не попало в расписание из-за наложения c другими событиями')

text=Text( width=80 , height=25)
text.grid(row=3, column=0, columnspan=5, padx=10, pady=15)
text.insert(1.0,'Дату и время вводить в формате HH.MM-DD.MM.YYYY\n')

A=StringVar()
B=StringVar()
C=StringVar()
a_label = Label(text="Введите название")
b_label = Label(text="Введите время и дату начала")
c_label = Label(text="Введите время и дату конца")

a_e=Entry(textvariable=A)
b_e=Entry(textvariable=B)
c_e=Entry(textvariable=C)


a_label.grid(row=0, column=0)
b_label.grid(row=0, column=1)
c_label.grid(row=0, column=2)

a_e.grid(row=1, column=0)
b_e.grid(row=1,column=1)
c_e.grid(row=1, column=2)

button=Button(text='Добавить событие', command=add_something)
button.grid(row=2,column=6)
button2=Button(text="Вывести расписание",command=vivod)
button2.grid(row=3,column=6,padx=10)


root.mainloop()