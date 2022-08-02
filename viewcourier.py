import mysql.connector
import tkinter as tk
from tkinter import ttk

r=tk.Tk()
r.title("Courier Details")
r.geometry("600x400")

connect=mysql.connector.connect(host="localhost",
user="root",
password="1234",
database="test")

conn=connect.cursor()
conn.execute("SELECT * FROM courier")

tree=ttk.Treeview(r)
tree['show'] = 'headings'

s = ttk.Style(r)
s.theme_use("clam")
s.configure(".", font=('Helvetica', 11))
s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))


tree["columns"]=('Sender Name','Sender Address','Name','Rollno')
#column
tree.column("Sender Name",width=160,minwidth=100,anchor=tk.CENTER)
tree.column("Sender Address",width=160,minwidth=100,anchor=tk.CENTER)
tree.column("Name",width=160,minwidth=100,anchor=tk.CENTER)
tree.column("Rollno",width=60,minwidth=100,anchor=tk.CENTER)


tree.heading("Sender Name",text="Sender Name",anchor=tk.CENTER)
tree.heading("Sender Address",text="Sender Address",anchor=tk.CENTER)
tree.heading("Name",text="Name",anchor=tk.CENTER)
tree.heading("Rollno",text="Rollno",anchor=tk.CENTER)

i=0
for ro in conn:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
    i=i+1

vsb = ttk.Scrollbar(r,orient="vertical")
vsb.configure(command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(fill='y',side = 'right')

hsb = ttk.Scrollbar(r,orient="horizontal")
hsb.configure(command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill='x',side = 'bottom')

tree.pack()
r.mainloop()