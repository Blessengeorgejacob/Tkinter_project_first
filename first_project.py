from tkinter import *
import tkinter as tk
from tkinter import ttk
import pymysql
import sqlite3

details= Tk()
details.title("DATA ENTRY FORM")
connection=pymysql.connect(host='localhost',user='root',passwd='',database='first_project')
c=connection.cursor()

background="grey"

frame=tk.Frame(details,bg=background)

label_first_name=tk.Label(frame,text="First Name :",font=('Times New Roman',14),bg=background)
entry_first_name=tk.Entry(frame)

label_last_name=tk.Label(frame,text="Last Name :",font=('Times New Roman',14),bg=background)
entry_last_name=tk.Entry(frame)

label_email_id=tk.Label(frame,text="Email Id :",font=('Times New Roman',14),bg=background)
entry_email_id=tk.Entry(frame)

label_age=tk.Label(frame,text="Age :",font=('Times New Roman',14),bg=background)
entry_age=tk.Entry(frame)

def data():
    first_name= entry_first_name.get()
    last_name= entry_last_name.get()
    email_id=entry_email_id.get()
    age=entry_age.get()

    data_query = "INSERT INTO `datainsert`(`first_name`, `last_name`, `email_id`, `age`) VALUES (%s,%s,%s,%s)"
    vals=(first_name,last_name,email_id,age)
    c.execute(data_query,vals)
    connection.commit()

button_details = tk.Button(frame,text="SUBMIT",font=('Times New Roman',14),bg='red',command = data)

label_first_name.grid(row=0,column=0)
entry_first_name.grid(row=0,column=1,pady=10,padx=30,sticky='nw')

label_last_name.grid(row=1,column=0)
entry_last_name.grid(row=1,column=1,pady=10,padx=30,sticky='nw')

label_email_id.grid(row=2,column=0,sticky='e')
entry_email_id.grid(row=2,column=1,pady=10,padx=30,sticky='nw')

label_age.grid(row=3,column=0,sticky='e')
entry_age.grid(row=3,column=1,pady=10,padx=30,sticky='nw')

button_details.grid(row=4,column=0,columnspan=1,sticky='nsew')
frame.grid(row=0,column=0)


details.mainloop()