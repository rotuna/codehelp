import csv
from tkinter import *
import tkinter as tk
import random
f=open("the office.csv","r")
a=csv.reader(f,delimiter=",")
seasons_data = []
for row in a:
        seasons_data.append(row)

master=tk.Tk()
master.geometry("600x600")
v= IntVar(master, "0")
values = {"Any Season" : "0",
        "Season 1" : "1",
        "Season 2" : "2",
        "Season 3" : "3",
        "Season 4" : "4",
        "Season 5" : "5",
        "Season 6" : "6",
        "Season 7" : "7",
        "Season 8" : "8",
        "Season 9" : "9",}

label2 = tk.Label(master, text='Select Season ')
label2.config(font=('helvetica', 17))

for (text, value) in values.items():
    r=int(value)
    Radiobutton(master, text = text, variable = v,
        value = value).grid(row=r+1,column=1)

label1 = tk.Label(master, text='Enter rating: ')
label1.config(font=('helvetica', 17))
entry1 = tk.Entry(master)

def FIND():
    rating=entry1.get()
    season=v.get()
    print(season)
    b=[]
    if season!=0:
        for i in seasons_data:
            r=float(i[3])
            if int(i[0])==season and r>=float(rating):
                b.append(i)
    else:
        for i in a:

            r=float(i[3])
            if r>=float(rating):
                b.append(i)
    print("b=",b)

    e=random.choice(b)
    print(e)

    s="Season "+e[0]+" Episode "+e[1]
    s2=e[2]
    s3="Rating: "+e[3]
    
    label3=tk.Label(master,text=s)
    label3.config(font=('helvetica',14))
    label3.grid(row=16,column=0)

    label4=tk.Label(master,text=s2)
    label4.config(font=('helvetica',14))
    label4.grid(row=17,column=0)

    label5=tk.Label(master,text=s3)
    label5.config(font=('helvetica',14))
    label5.grid(row=18,column=0)
    
    

button1 = tk.Button(master,text='Find episode', command=FIND, font=('helvetica', 9, 'bold'))
button2 = tk.Button(master,text='End', command=FIND, font=('helvetica', 9, 'bold'))

label2.grid(row=0,column=0)
label1.grid(row=12,column=0)
entry1.grid(row=12,column=1)
button1.grid(row=14,column=0)
while True:
    master.mainloop()

f.close()
