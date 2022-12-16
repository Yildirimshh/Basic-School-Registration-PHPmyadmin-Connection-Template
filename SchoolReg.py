import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from tkinter import *


window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()
show_frame(page1)

# ======================================================== Page 1 ========================================================

page1.config(background="black")

class login():
    def ok(login):
        if login.u1.get() == "" or login.u2.get() == "" :
            messagebox.showerror("error","Loging Success", parent=login.root)
        elif login.u1.get() != "admin" or login.u2.get() != "112233":
            messagebox.showerror("error","Loging Success", parent=login.root)
        else:
            messagebox.showinfo("Welcom", "Welcome {login.uname.get()}")

pag1_label = Label(page1, text='Username', fg="white", bg="black", font=("Arial", 15, "bold"))
pag1_label.place(x=630, y=200)
pag1_label2 = Label(page1, text="Password", fg="white", bg="black", font=("Arial", 15, "bold"))
pag1_label2.place(x=630, y=285)
pag1_label3 = Label(page1, text="_"*30, fg="white", bg="black", font=('Arial', 15, 'bold'))
pag1_label3.place(x=515, y=375)
u1 = Entry(window, width=40)
u1.place(x=560, y=250)
u2 = Entry(window, width=40)
u2.place(x=560, y=335)

pg1_button = Button(window, text="Login", highlightthickness=1, highlightbackground = "white", fg="white", bg="black", width=15, font=('Arial', 13, 'bold'), command= login)
pg1_button.place(x=600, y=450)
pg2_button = Button(window, text="Next", highlightthickness=1, highlightbackground = "white", fg="white", bg="black", width=15, font=('Arial', 13, 'bold'), command=lambda: show_frame(page2))
pg2_button.place(x=600, y=500)

# ======================================================== Page 2 ========================================================

page2.config(background='black')

def Add():
    number = e1.get()
    name = e2.get()
    surename = e3.get()
    school_no = e4.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="studentdata")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  student (Number,Name,Surename,School_no) VALUES (%s, %s, %s, %s)"
       val = (number,name,surename,school_no)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Warning", "Register Successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def update():
    number = e1.get()
    name = e2.get()
    surename = e3.get()
    school_no = e4.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="studentdata")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update  student set Number= %s,Name= %s,Surename= %s where ScoolNo= %s"
       val = (number,name,surename,school_no)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Warning", "Update Was Successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def delete():
    studid = e1.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="studentdata")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from student where Number = %s"
       val = (studid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Warning", "Delete Was Successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

Label(page2, text="Basic School Info Sistem", fg="white", bg="black", font=("Arial Bold", 30)).place(x=450, y=55)
Label(page2, text="Number", fg="white", bg="black", width=15, font=15).place(x=25, y=130)
Label(page2, text="Name", fg="white", bg="black", width=15, font=15).place(x=25, y=160)
Label(page2, text="Surename", fg="white", bg="black", width=15, font=15).place(x=25, y=190)
Label(page2, text="School No", fg="white", bg="black", width=15, font=15).place(x=25, y=220)

pg2_button1 = Button(page2, text="Ekle", bd=4, fg="white", bg="black", height=1, width=10, font=('Arial', 12), command= Add)
pg2_button1.place(x=300, y=345)
pg2_button2 = Button(page2, text="Güncelle", bd=4, fg="white", bg="black", height=1, width=10, font=('Arial', 12), command= update)
pg2_button2.place(x=425, y=345)
pg2_button3 = Button(page2, text="Sil", bd=4, bg="black", height=1, width=10, fg="red", font=('Arial', 12), command= delete)
pg2_button3.place(x=550, y=345)
pg2_button4 = Button(page2, text="Sonraki", bd=4, fg="white", bg="black", height=1, width=10, font=('Arial', 12, 'bold'), command=lambda: show_frame(page3))
pg2_button4.place(x=675, y=345)

cols = ("Number", "Name", "Surename","School No")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="silver", forground = "black", rowheight = 25, fieldbackground = "silver", font = ('Arial', 12))
style.map("Treeview", background= {("selected", "black")})
listBox = ttk.Treeview(page2, columns=cols, show='headings')

e1 = Entry(page2, width=30)
e1.place(x=200, y=130)
e2 = Entry(page2, width=30)
e2.place(x=200, y=160)
e3 = Entry(page2, width=30)
e3.place(x=200, y=190)
e4 = Entry(page2, width=30)
e4.place(x=200, y=220)

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select["Number"])
    e2.insert(0,select["Name"])
    e3.insert(0,select["Surename"])
    e4.insert(0,select["School No"])

for col in cols:
    
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=275, y=400)
      
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="studentdata")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT Number,Name,Surename,School_no FROM student")
        records = mycursor.fetchall()
        print(records)
 
        for i, (id,stname, course,fee) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, stname, course, fee))
            mysqldb.close()
show()
listBox.bind('<Double-Button-1>',GetValue)

# ======================================================== Page 3 ========================================================

page3.config(background='black')

pag3_label = Label(page3, text="Main Informatin", bg="black", fg="white", font=('Arial', 30, 'bold'))
pag3_label.place(x=500, y=20)
pg3_button = Button(page3, text='Geri', bd=4, fg="white", bg="black", width=15, font=('Arial', 12, 'bold'), command=lambda: show_frame(page2))
pg3_button.place(x=600, y=650)

cols = ("Number", "Name", "Surename","School Name")
listBox = ttk.Treeview(page3, columns=cols, show='headings', height=20)

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=2, column=0, columnspan=2)
    listBox.place(x=275, y=100)
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="studentdata")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT Number,Name,Surename,School_no FROM student")
        records = mycursor.fetchall()
        print(records)
 
        for i, (number,name, surename,school_no) in enumerate(records, start=1):
            listBox.insert("", "end", values=(number, name, surename, school_no))
            mysqldb.close()

show()
listBox.bind('<Double-Button-1>',GetValue)

window.mainloop()
