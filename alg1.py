from tkinter import *
from tkinter import messagebox
 
t = 0
u = 0
o = 0
p = 0
def algorithm():
    global t
    global u

    if int(a.get())>int(s.get()):
        t+=1
    elif int(a.get())<int(s.get()):
        u+=1
    else:
        pass
        


    if int(d.get())>int(f.get()):
        t+=1
    elif int(d.get())<int(f.get()):
        u+=1
    else:
        pass


    if int(g.get())>int(h.get()):
        t+=1
    elif int(g.get())<int(h.get()):
        u+=1
    else:
        pass


    if int(j.get())>int(k.get()):
        u+=1
    elif int(j.get())<int(k.get()):
        t+=1
    else:
        pass

    if int(l.get())>int(z.get()):
        t+=1
    elif int(l.get())<int(z.get()):
        u+=1
    else:
        pass

    if int(x.get())>int(c.get()):
        t+=1
    elif int(x.get())<int(c.get()):
        u+=1
    else:
        pass

    if int(v.get())>int(b.get()):
        t+=1
    elif int(v.get())<int(b.get()):
        u+=1
    else:
        pass

    if t>u:
        messagebox.showinfo("GUI Python","Выиграет" + " " + club1.get())
    elif t<u:
        messagebox.showinfo("GUI Python","Выиграет" + " " + club2.get())
    else:
        messagebox.showinfo("GUI Python", "Owibka")

def copy():
    global o
    global p
    o = o + ((int(a.get())*0.35)+((int(d.get())*0.05)+((int(g.get())*0.15)+((int(j.get())*0.10)+((int(l.get())*0.005)+((int(x.get())*0.15)+((int(v.get())*0.195))))))))
    p = p + ((int(s.get())*0.35)+((int(f.get())*0.05)+((int(h.get())*0.15)+((int(k.get())*0.10)+((int(z.get())*0.005)+((int(c.get())*0.15)+((int(b.get())*0.195))))))))
    print(messagebox.showinfo("GUI Python",str(o) + "%" + " " + "vs" + " " + str(p) + "%"))                       
                
    

    
root = Tk()
root.title("Прогноз от Бауыржана и Нарула")
 
club1 = StringVar()
club2 = StringVar()
a = StringVar()
s = StringVar()
d = StringVar()
f = StringVar()
g = StringVar()
h = StringVar()
j = StringVar()
k = StringVar()
l = StringVar()
z = StringVar()
x = StringVar()
c = StringVar()
v = StringVar()
b = StringVar()

 
club1_label = Label(text="Введите первую команду:")
club2_label = Label(text="Введите вторую команду:")
a_label = Label(text="Разница голов:")
s_label = Label(text="Разница голов:")
d_label = Label(text="Офсайды:")
f_label = Label(text="Офсайды:")
g_label = Label(text="Угловые:")
h_label = Label(text="Угловые:")
j_label = Label(text="Фолы:")
k_label = Label(text="Фолы:")
l_label = Label(text="Всего передач:")
z_label = Label(text="Всего передач:")
x_label = Label(text="Отборы:")
c_label = Label(text="Отборы:")
v_label = Label(text="Удары в створ:")
b_label = Label(text="Удары в створ:")
 
club1_label.grid(row=0, column=0, sticky="w")
club2_label.grid(row=0, column=2, sticky="w")
a_label.grid(row=1, column=0, sticky="w")
s_label.grid(row=1, column=2, sticky="w")
d_label.grid(row=2, column=0, sticky="w")
f_label.grid(row=2, column=2, sticky="w")
g_label.grid(row=3, column=0, sticky="w")
h_label.grid(row=3, column=2, sticky="w")
j_label.grid(row=4, column=0, sticky="w")
k_label.grid(row=4, column=2, sticky="w")
l_label.grid(row=5, column=0, sticky="w")
z_label.grid(row=5, column=2, sticky="w")
x_label.grid(row=6, column=0, sticky="w")
c_label.grid(row=6, column=2, sticky="w")
v_label.grid(row=7, column=0, sticky="w")
b_label.grid(row=7, column=2, sticky="w")

 
club1_entry = Entry(textvariable=club1)
club2_entry = Entry(textvariable=club2)
a_entry = Entry(textvariable=a)
s_entry = Entry(textvariable=s)
d_entry = Entry(textvariable=d)
f_entry = Entry(textvariable=f)
g_entry = Entry(textvariable=g)
h_entry = Entry(textvariable=h)
j_entry = Entry(textvariable=j)
k_entry = Entry(textvariable=k)
l_entry = Entry(textvariable=l)
z_entry = Entry(textvariable=z)
x_entry = Entry(textvariable=x)
c_entry = Entry(textvariable=c)
v_entry = Entry(textvariable=v)
b_entry = Entry(textvariable=b)

 
club1_entry.grid(row=0,column=1, padx=5, pady=5)
club2_entry.grid(row=0,column=3, padx=5, pady=5)
a_entry.grid(row=1,column=1, padx=5, pady=5)
s_entry.grid(row=1,column=3, padx=5, pady=5)
d_entry.grid(row=2,column=1, padx=5, pady=5)
f_entry.grid(row=2,column=3, padx=5, pady=5)
g_entry.grid(row=3,column=1, padx=5, pady=5)
h_entry.grid(row=3,column=3, padx=5, pady=5)
j_entry.grid(row=4,column=1, padx=5, pady=5)
k_entry.grid(row=4,column=3, padx=5, pady=5)
l_entry.grid(row=5,column=1, padx=5, pady=5)
z_entry.grid(row=5,column=3, padx=5, pady=5)
x_entry.grid(row=6,column=1, padx=5, pady=5)
c_entry.grid(row=6,column=3, padx=5, pady=5)
v_entry.grid(row=7,column=1, padx=5, pady=5)
b_entry.grid(row=7,column=3, padx=5, pady=5)

 
 
message_button = Button(text="Start", command=algorithm)
message_button.grid(row=8,column=3, padx=5, pady=5, sticky="e")


message1_button = Button(text="Percent", command=copy)
message1_button.grid(row=8,column=0, padx=5, pady=5, sticky="e")
     
root.mainloop()
