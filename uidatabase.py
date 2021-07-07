from os import error
import tkinter
from main import show_all
import tkinter as tk
from tkinter import Label, messagebox
import sqlite3
import time

conn = sqlite3.connect('base.db')
c = conn.cursor()
'''
c.execute("DELETE FROM list WHERE rowid=1")
c.execute("DELETE FROM list WHERE rowid=2")
c.execute("DELETE FROM list WHERE rowid=3")
conn.commit()
'''


def skip():
    app.destroy()
    basemainapp()

def basemainapp():
    mainApp = tk.Tk()
    mainApp.title('Database')

    #destryoing previus frame/app
    canvas = tk.Canvas(mainApp)
    c.execute("SELECT * FROM list")
    datas = c.fetchall()
    for i in datas:
        label = Label(mainApp, text=i[0] + "  " + i[1] + "\t" + i[2] + "\t        " + str(i[3]))
        label.pack()
        
    mainApp.mainloop()



app = tk.Tk()
app.title('App')

canvas = tk.Canvas(app, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(app, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.065)

titletext = tk.Label(frame, text="Welcome!\n Please make sure to input your contact datas\n _______________________________")
titletext.place(relx=0.035,rely=0.05)
titletext.config(font=("Courier", 18))


#Inputs

e1 = tk.Entry(frame)
e1.place(relwidth=0.4, relx=0.3, rely=0.2)
e2 = tk.Entry(frame)
e2.place(relwidth=0.4, relx=0.3, rely=0.25)
e3 = tk.Entry(frame)
e3.place(relwidth=0.4, relx=0.3, rely=0.3)
e4 = tk.Entry(frame)
e4.place(relwidth=0.4, relx=0.3, rely=0.35)

#Labels which defines inputs

uname = tk.Label(frame, text="First name:")
uname.place(relx=0.11, rely=0.205)
uname.config(font=("Courier", 15))

lname = tk.Label(frame, text="Last name:")
lname.place(relx=0.125, rely=0.256)
lname.config(font=("Courier", 15))

lname = tk.Label(frame, text="Email:")
lname.place(relx=0.19, rely=0.306)
lname.config(font=("Courier", 15))

phoneNumber = tk.Label(frame, text="Phone number:")
phoneNumber.place(relx=0.077, rely=0.356)
phoneNumber.config(font=("Courier", 15))

#error message

def emptyfields(wtitle, alert):
    messagebox.showwarning(wtitle, alert)

def gottendata():
    ndata = e1.get()
    lndata = e2.get()
    edata = e3.get()
    pdata = e4.get()
    datalist = [ndata, lndata, edata, pdata]
    print(datalist)
    #for x in datalist:
        #print(x)

    errornotifier = None
    if len(e1.get()) < 3:
        emptyfields("Empty field", "Empty fields")
    elif len(e2.get()) < 4:
        emptyfields("Empty field", "Empty fields")
    elif len(e3.get()) < 6:
        emptyfields("Empty field", "Empty fields")
    elif len(e4.get()) < 4:
        emptyfields("Empty field", "Empty fields")
    else:
        btn.destroy()
        c.execute("INSERT INTO list VALUES(?,?,?,?)", datalist)
        conn.commit()
        query = c.fetchall()
        print(query)
        basemainapp()

#Button

btn = tk.Button(app, text="CREATE CONTACT", padx=50, pady=5, fg="#263D42", command=gottendata)
btn.place(relwidth=0.2, relx=0.4, rely=0.4)

skipbtn = tk.Button(app, text="SKIP", padx=50, pady=5, fg="#263D42", command=skip)
skipbtn.place(relwidth=0.2, relx=0.4, rely=0.45)


app.mainloop()
print(c.fetchall())
