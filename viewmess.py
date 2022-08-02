import mysql.connector
import tkinter as tk
from tkinter import ttk

r=tk.Tk()
r.title("Mess Details")
r.geometry("600x400")

connect=mysql.connector.connect(host="localhost",
user="root",
password="1234",
database="test")

conn=connect.cursor()
conn.execute("SELECT * FROM mess")

tree=ttk.Treeview(r)
tree['show'] = 'headings'

s = ttk.Style(r)
s.theme_use("clam")
s.configure(".", font=('Helvetica', 11))
s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))


tree["columns"]=('Roll No','Bill Amount','Veg / Non Veg','Menu Type')
#column
tree.column("Roll No",width=100,minwidth=100,anchor=tk.CENTER)
tree.column("Bill Amount",width=160,minwidth=100,anchor=tk.CENTER)
tree.column("Veg / Non Veg",width=160,minwidth=100,anchor=tk.CENTER)
tree.column("Menu Type",width=160,minwidth=100,anchor=tk.CENTER)


tree.heading("Roll No",text="Roll No",anchor=tk.CENTER)
tree.heading("Bill Amount",text="Bill Amount",anchor=tk.CENTER)
tree.heading("Veg / Non Veg",text="Veg / Non Veg",anchor=tk.CENTER)
tree.heading("Menu Type",text="Menu Type",anchor=tk.CENTER)

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