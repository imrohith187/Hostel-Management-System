from tkinter import *;
from tkinter import messagebox
import mysql.connector

top=Tk()
top.geometry("450x300")
top.title("Student Sharing")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  db="test"
)
c=mydb.cursor()
class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()
        
        master.configure(bg='#28282B')
         #lables

        self.Roomno = Label(master, text = "Roomno",font = ("Arial", 11))
        self.Roomno.place(x = 25,y = 50) 
        self.Roomno.config(bg="#28282B",fg="white") 

        self.Studentname = Label(master, text = "Block",font = ("Arial", 11))
        self.Studentname .place(x = 25, y = 100) 
        self.Studentname.config(bg="#28282B",fg="white")  

        self.block = Label(master, text = "Rollno",font = ("Arial", 11))
        self.block.place(x = 25,y = 150)
        self.block.config(bg="#28282B",fg="white")   
         

        #entities
        self.e1 = Entry(master,font = ('calibre',10,'normal'))
        self.e1.place(x = 130, y = 50,height=22, width=140)

        self.e2 = Entry(master,font = ('calibre',10,'normal')) 
        self.e2.place(x = 130, y = 100 ,height=22, width=140)

        self.e3 = Entry(master,font = ('calibre',10,'normal')) 
        self.e3.place(x = 130, y = 150 ,height=22, width=140)

        #Button

        self.mybutton =Button(master,text="Submit",command=self.submit,activebackground = "black", activeforeground = "white")
        self.mybutton.place(x=110,y=200)
        self.mybutton.config(height=2,width=20)

    def submit(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        db="test"
        )
        c=mydb.cursor()
        sql = "INSERT INTO student_sharing (roomno,block,rollno) VALUES (%s, %s ,%s)"
        val = (self.e1.get(), self.e2.get(),self.e3.get())
        c.execute(sql,val)
        mydb.commit()
        mydb.close()     
        messagebox.showinfo("","Datas Inserted")   

a=App(top)
top.resizable(0,0)
mydb.commit()
mydb.close()  
top.mainloop()