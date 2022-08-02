import mysql.connector
import tkinter as tk
from tkinter import ttk

r=tk.Tk()
r.title("Student Details")
r.geometry("600x400")

connect=mysql.connector.connect(host="localhost",
user="root",
password="1234",
database="test")

conn=connect.cursor()
conn.execute("SELECT * FROM student_info")

tree=ttk.Treeview(r)
tree['show'] = 'headings'

s = ttk.Style(r)
s.theme_use("clam")
s.configure(".", font=('Helvetica', 11))
s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))


tree["columns"]=('Name','Rollno','Age','Bloodgroup','Email','Phoneno')
#column
tree.column("Name",width=80,minwidth=50,anchor=tk.CENTER)
tree.column("Rollno",width=80,minwidth=50,anchor=tk.CENTER)
tree.column("Age",width=80,minwidth=50,anchor=tk.CENTER)
tree.column("Bloodgroup",width=100,minwidth=50,anchor=tk.CENTER)
tree.column("Email",width=125,minwidth=50,anchor=tk.CENTER)
tree.column("Phoneno",width=100,minwidth=50,anchor=tk.CENTER)
# heading
tree.heading("Name",text="Name",anchor=tk.CENTER)
tree.heading("Rollno",text="Rollno",anchor=tk.CENTER)
tree.heading("Age",text="Age",anchor=tk.CENTER)
tree.heading("Bloodgroup",text="Bloodgroup",anchor=tk.CENTER)
tree.heading("Email",text="Email",anchor=tk.CENTER)
tree.heading("Phoneno",text="Phoneno",anchor=tk.CENTER)

i=0
for ro in conn:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
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

# import mysql.connector
# import tkinter as tk
# from tkinter import ttk

# r=tk.Tk()
# r.title("Student Details")
# r.geometry("600x400")

# connect=mysql.connector.connect(host="localhost",
# user="root",
# password="1234",
# database="test")

# conn=connect.cursor()
# conn.execute("SELECT * FROM student_info INNER JOIN room_info ON room_info.rollno=student_info.rollno")

# tree=ttk.Treeview(r)
# tree['show'] = 'headings'

# s = ttk.Style(r)
# s.theme_use("clam")
# s.configure(".", font=('Helvetica', 11))
# s.configure("Treeview.Heading", foreground='black',font=('Helvetica', 11,"bold"))


# tree["columns"]=('Name','Rollno','Age','Bloodgroup','Email','Phoneno','Roll No','Room No','Block','Room Type')
# #column
# tree.column("Name",width=80,minwidth=50,anchor=tk.CENTER)
# tree.column("Rollno",width=80,minwidth=50,anchor=tk.CENTER)
# tree.column("Age",width=80,minwidth=50,anchor=tk.CENTER)
# tree.column("Bloodgroup",width=100,minwidth=50,anchor=tk.CENTER)
# tree.column("Email",width=125,minwidth=50,anchor=tk.CENTER)
# tree.column("Phoneno",width=100,minwidth=50,anchor=tk.CENTER)
# tree.column("Roll No",width=100,minwidth=50,anchor=tk.CENTER)
# tree.column("Room no",width=100,minwidth=50,anchor=tk.CENTER)
# tree.column("Block",width=100,minwidth=50,anchor=tk.CENTER)
# tree.column("Room Type",width=100,minwidth=50,anchor=tk.CENTER)
# # heading
# tree.heading("Name",text="Name",anchor=tk.CENTER)
# tree.heading("Rollno",text="Rollno",anchor=tk.CENTER)
# tree.heading("Age",text="Age",anchor=tk.CENTER)
# tree.heading("Bloodgroup",text="Bloodgroup",anchor=tk.CENTER)
# tree.heading("Email",text="Email",anchor=tk.CENTER)
# tree.heading("Phoneno",text="Phoneno",anchor=tk.CENTER)
# tree.heading("Roll No",text="Roll No",anchor=tk.CENTER)
# tree.heading("Room no",text="Room no",anchor=tk.CENTER)
# tree.heading("Block",text="Block",anchor=tk.CENTER)
# tree.heading("Room Type",text="Room Type",anchor=tk.CENTER)

# i=0
# for ro in conn:
#     tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9]))
#     i=i+1

# vsb = ttk.Scrollbar(r,orient="vertical")
# vsb.configure(command=tree.yview)
# tree.configure(yscrollcommand=vsb.set)
# vsb.pack(fill='y',side = 'right')

# hsb = ttk.Scrollbar(r,orient="horizontal")
# hsb.configure(command=tree.xview)
# tree.configure(xscrollcommand=hsb.set)
# hsb.pack(fill='x',side = 'bottom')

# tree.pack()
# r.mainloop()