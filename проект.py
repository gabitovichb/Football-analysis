from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import wikipedia
import webbrowser
import tkinter
import random
import time






root = tkinter.Tk()
root.title("Liga de Fútbol Profesional")
root.geometry("300x380")


logo = PhotoImage(file="C:/Users/Бауыржан/Desktop/прога финал проект/Betting-Odds-for-Barclays-Premier-League-Leicester-City-vs-Burnley.png")
logo1 = Label(root, image=logo)

    
e=["C:/Users/Бауыржан/esktop/прога финал проект/spurs-blue-no-text-300x300.png","C:/Users/Бауыржан/Desktop/прога финал проект/images.png","C:/Users/Бауыржан/Desktop/прога финал проект/images (1).png","C:/Users/Бауыржан/Desktop/прога финал проект/images (5).png","C:/Users/Бауыржан/Desktop/прога финал проект/images (3).png","C:/Users/Бауыржан/Desktop/прога финал проект/Без названия (1).png","C:/Users/Бауыржан/Desktop/прога финал проект/Без названия (2).png","C:/Users/Бауыржан/Desktop/прога финал проект/Без названия (3).png","C:/Users/Бауыржан/Desktop/прога финал проект/Без названия (4).png"] 
m=["Это Тоттенхэм?","Это Суенси?","Это Фулхэм?","Это Халл сити?","Это Норвич Сити?","Это Сандерленд?","Это Вулверхэмптон?","Это Ман сити?","Это Брайтон?"] 


def moregames(): 
    w = webbrowser.open('https://play.google.com/store/search?q=%D1%83%D0%B3%D0%B0%D0%B4%D0%B0%D0%B9%20%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%83&c=apps')
def olimp(): 
    w = webbrowser.open('https://olimp.kz/')
def sub():
    w = webbrowser.open('https://www.premierleague.com/news')


def play(): 

    v = tkinter.Toplevel() 
    v.title("GAMEEEE") 
    v.geometry("700x500") 



    r6 = Label(v,text = "Чья это эмблема???",fg="green",bg="red") 
    r6.config(font=("Papyrus",23)) 
    r6.pack() 


    pk = random.choice(m) 

    r5 = Label(v,text = pk,fg="blue",bg="white") 
    r5.config(font=("Papyrus",20)) 
    r5.place(x=230,y=350) 


    pl = random.choice(e) 

    logo9 = PhotoImage(file=pl) 
    logo10 = Label(v,image=logo9) 





    bttn56 = Button(v, text="True",command=play) 
    bttn56.config(width=20, height=2, bg="black", fg="white") 



    bttn57 = Button(v, text="False",command=v.destroy) 
    bttn57.config(width=20, height=2, bg="black", fg="white") 

    logo10.pack() 
    bttn56.pack() 
    bttn56.place(x=140,y=450) 
    bttn57.pack() 
    bttn57.place(x=400,y=450) 

    r5.pack() 

    v.mainloop() 



def inst(): 
    o = tkinter.Toplevel() 
    o.title("34938493289") 
    o.geometry("544x342") 
    o.resizable(0,0) 
    logo6 = PhotoImage(file="C:/Users/Бауыржан/Desktop/прога финал проект/sdsdsdsd.png") 
    logo7 = Label(o, image=logo6) 
    logo7.pack() 
    o.mainloop() 




def game(): 

    s = tkinter.Toplevel() 
    s.title("....") 
    s.geometry("700x400") 
    s.resizable(0,0) 
    r7 = Label(s,text = "!!!Угадай Команду!!!",fg="white",bg="grey") 
    r7.config(font=("Papyrus",24)) 


    logo = PhotoImage(file="C:/Users/Бауыржан/Desktop/прога финал проект/Chelsea-Willian-Hazard-700x434.png") 
    logo1 = Label(s, image=logo) 


    bttn4 = Button(s, text="Начать Игру",command=play) 
    bttn4.config(width=20, height=3, bg="blue", fg="white") 

    bttn3 = Button(s, text="Правила игры",command=inst) 
    bttn3.config(width=20, height=3, bg="blue", fg="white") 


    bttn5 = Button(s, text="Больше игр",command=moregames) 
    bttn5.config(width=20, height=1, bg="black", fg="white") 

    logo1.pack() 
    bttn4.pack() 
    bttn4.place(x=0,y=0) 
    bttn3.pack() 
    bttn3.place(x=560,y=0) 
    bttn5.pack() 
    bttn5.place(x=550,y=373) 

    r7.pack() 
    s.mainloop() 



 




def but(): 
    window = Tk() 
    window.title("Table") 
    window.geometry("465x576") 
    window.resizable(False, False) 
    canvas = Canvas(window, width = 465, height = 576) 
    canvas.pack() 
    y=0 
    while y<1000: 
        x=0 
        while x<572: 
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")
            x=x+33 
        y=y+27 
    a0=canvas.create_text(54, 48, text="Liverpool", fill="purple", font=("Lucida Handwriting","14"))
    a1= canvas.create_text(85, 74, text="Manchester City", fill="purple", font=("Lucida Handwriting", "14"))
    a2=canvas.create_text(59, 100, text="Tottenham", fill="purple", font=("Lucida Handwriting","14"))
    a3= canvas.create_text(43, 128, text="Chelsea", fill="purple", font=("Lucida Handwriting", "14"))
    a4=canvas.create_text(43, 154, text="Arsenal", fill="purple", font=("Lucida Handwriting","14"))
    a5= canvas.create_text(100, 180, text="Manchester United", fill="purple", font=("Lucida Handwriting", "14"))
    a6=canvas.create_text(89, 208, text="Wolverhampton", fill="purple", font=("Lucida Handwriting","14"))
    a7= canvas.create_text(45, 236, text="Everton", fill="purple", font=("Lucida Handwriting", "14"))
    a8=canvas.create_text(45, 264, text="Watford", fill="purple", font=("Lucida Handwriting","14"))
    a9= canvas.create_text(69, 288, text="Leicester City", fill="purple", font=("Lucida Handwriting", "14"))
    a10=canvas.create_text(92, 316, text="West Ham United", fill="purple", font=("Lucida Handwriting","14"))
    a11= canvas.create_text(80, 344, text="Crystal Palace", fill="purple", font=("Lucida Handwriting", "14"))
    a12=canvas.create_text(93, 370, text="Newcastle United", fill="purple", font=("Lucida Handwriting","14"))
    a13= canvas.create_text(75, 396, text="Bournemouth", fill="purple", font=("Lucida Handwriting", "14"))
    a14=canvas.create_text(43, 424, text="Burnley", fill="purple", font=("Lucida Handwriting","14"))
    a15= canvas.create_text(73, 452, text="Southampton", fill="purple", font=("Lucida Handwriting", "14"))
    a16=canvas.create_text(50, 478, text="Brighton", fill="purple", font=("Lucida Handwriting","14"))
    a17= canvas.create_text(61, 506, text="Cardiff City", fill="purple", font=("Lucida Handwriting", "14"))
    a18=canvas.create_text(42, 532, text="Fulham", fill="purple", font=("Lucida Handwriting","14"))
    a19= canvas.create_text(72, 560, text="Huddersfield", fill="purple", font=("Lucida Handwriting", "14"))

    a20= canvas.create_text(215, 18, text="И", fill="purple", font=("Lucida Handwriting", "14"))
    a21= canvas.create_text(246, 18, text="В", fill="purple", font=("Lucida Handwriting", "14"))
    a22= canvas.create_text(280, 18, text="Н", fill="purple", font=("Lucida Handwriting", "14"))
    a23= canvas.create_text(313, 18, text="П", fill="purple", font=("Lucida Handwriting", "14"))
    a24= canvas.create_text(346, 18, text="ЗМ", fill="purple", font=("Lucida Handwriting", "14"))
    a25= canvas.create_text(380, 18, text="ПМ", fill="purple", font=("Lucida Handwriting", "14"))
    a26= canvas.create_text(412, 18, text="РМ", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 18, text="О", fill="purple", font=("Lucida Handwriting", "14"))
    
    a27= canvas.create_text(215, 45, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 45, text="28", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 45, text="7", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 45, text="1", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 45, text="84", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 45, text="20", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 45, text="64", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 45, text="91", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 74, text="35", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 74, text="29", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 74, text="2", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 74, text="4", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 74, text="89", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 74, text="22", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 74, text="67", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 74, text="89", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 100, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 100, text="23", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 100, text="1", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 100, text="12", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 100, text="65", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 100, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 100, text="29", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 100, text="70", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 128, text="35", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 128, text="20", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 128, text="7", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 128, text="8", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 128, text="59", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 128, text="38", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 128, text="21", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 128, text="67", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 154, text="35", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 154, text="20", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 154, text="6", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 154, text="9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 154, text="69", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 154, text="46", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 154, text="23", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 154, text="66", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 180, text="35", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 180, text="19", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 180, text="7", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 180, text="9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 180, text="63", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 180, text="50", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 180, text="13", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 180, text="64", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 208, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 208, text="15", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 208, text="9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 208, text="12", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 208, text="46", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 208, text="44", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 208, text="2", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 208, text="54", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 236, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 236, text="14", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 236, text="8", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 236, text="14", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 236, text="50", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 236, text="44", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 236, text="6", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 236, text="50", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 264, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 264, text="14", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 264, text="8", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 264, text="14", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 264, text="51", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 264, text="52", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 264, text="-1", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 264, text="50", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 288, text="35", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 288, text="14", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 288, text="6", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 288, text="15", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 288, text="48", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 288, text="47", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 288, text="1", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 288, text="48", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 316, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 316, text="13", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 316, text="7", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 316, text="16", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 316, text="45", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 316, text="54", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 316, text="-9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 316, text="46", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 344, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 344, text="12", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 344, text="7", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 344, text="17", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 344, text="43", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 344, text="48", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 344, text="-5", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 344, text="43", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 370, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 370, text="11", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 370, text="9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 370, text="16", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 370, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 370, text="45", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 370, text="-9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 370, text="42", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 396, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 396, text="12", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 396, text="6", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 396, text="18", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 396, text="52", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 396, text="65", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 396, text="-13", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 396, text="42", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 424, text="35", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 424, text="11", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 424, text="7", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 424, text="17", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 424, text="44", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 424, text="62", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 424, text="-18", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 424, text="40", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 452, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 452, text="9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 452, text="11", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 452, text="16", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 452, text="44", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 452, text="61", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 452, text="-17", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 452, text="38", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 478, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 478, text="9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 478, text="8", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 478, text="19", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 478, text="33", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 478, text="55", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 478, text="-22", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 478, text="35", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 506, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 506, text="9", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 506, text="4", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 506, text="23", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 506, text="30", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 506, text="66", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 506, text="-36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 506, text="31", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 532, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 532, text="7", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 532, text="5", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 532, text="24", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 532, text="34", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 532, text="76", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 532, text="-42", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 532, text="26", fill="purple", font=("Lucida Handwriting", "14"))

    a27= canvas.create_text(215, 560, text="36", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(246, 560, text="3", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(280, 560, text="5", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(313, 560, text="28", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(346, 560, text="20", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(380, 560, text="74", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(412, 560, text="-54", fill="purple", font=("Lucida Handwriting", "14"))
    a27= canvas.create_text(445, 560, text="14", fill="purple", font=("Lucida Handwriting", "14"))

    window.mainloop()
    
def ext():
    root.destroy()




bttn5 = Button(root, text="СТАВЬ",command=olimp)
bttn5.config(width=10, height=1, bg="red", fg="black")


bttn4 = Button(root, text="НОВОСТИ",command=sub)
bttn4.config(width=10, height=1, bg="blue", fg="white")

bttn3 = Button(root, text="ТАБЛИЦА",command=but)
bttn3.config(width=10, height=1, bg="yellow", fg="blue")

bttn2 = Button(root, text="ИГРА",command=game)
bttn2.config(width=10, height=1, bg="pink", fg="white")

bttn1 = Button(root, text="ВЫЙТИ", command=ext)
bttn1.config(width=10, height=1, bg="green", fg="black")



logo1.pack()


bttn5.pack()
bttn5.place(x=0,y=0)

bttn4.pack()
bttn4.place(x=0,y=243)

bttn3.pack()
bttn3.place(x=225,y=0)

bttn2.pack()
bttn2.place(x=112,y=121)

bttn1.pack()
bttn1.place(x=225,y=243)



root.mainloop()





