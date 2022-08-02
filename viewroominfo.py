import mysql.connector
import tkinter as tk
from tkinter import ttk

r=tk.Tk()
r.title("Room Details")
r.geometry("600x400")

connect=mysql.connector.connect(host="localhost",
user="root",
password="1234",
database="test")

conn=connect.cursor()
conn.execute("SELECT * FROM room_info")

tree=ttk.Treeview(r)
tree['show'] = 'headings'

s = ttk.Style(r)
s.theme_use("clam")
s.configure(".", font=('Helvetica', 11))
s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))


tree["columns"]=('Rollno','Roomno','Block','RoomType')
#column
tree.column("Rollno",width=80,minwidth=50,anchor=tk.CENTER)
tree.column("Roomno",width=80,minwidth=50,anchor=tk.CENTER)
tree.column("Block",width=80,minwidth=50,anchor=tk.CENTER)
tree.column("RoomType",width=100,minwidth=50,anchor=tk.CENTER)
# heading
tree.heading("Rollno",text="Rollno",anchor=tk.CENTER)
tree.heading("Roomno",text="Roomno",anchor=tk.CENTER)
tree.heading("Block",text="Block",anchor=tk.CENTER)
tree.heading("RoomType",text="RoomType",anchor=tk.CENTER)

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