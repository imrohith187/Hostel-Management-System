from tkinter import *;
from tkinter import messagebox
import mysql.connector

top=Tk()
top.geometry("450x500")
top.title("Insert Courier")

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
        # master.configure(bg='yellow')
        master.configure(background='#28282B')
        #values
        self.radio = IntVar()  

         #lables
        self.Rollno = Label(master, text = "Sender Name",font = ("Arial", 11))
        self.Rollno.place(x = 25,y = 50)
        self.Rollno.config(bg="#28282B",fg="white")  

        self.Roomno = Label(master, text = "Sender Address",font = ("Arial", 11))
        self.Roomno .place(x = 25, y = 100) 
        self.Roomno.config(bg="#28282B",fg="white") 

        self.block = Label(master, text = "Name",font = ("Arial", 11))
        self.block.place(x = 25,y = 150)
        self.block.config(bg="#28282B",fg="white") 

        self.roomtype = Label(master, text = "Roll No",font = ("Arial", 11))
        self.roomtype.place(x = 25,y = 200)
        self.roomtype.config(bg="#28282B",fg="white") 
         

        #entities
        self.e1 = Entry(master,font = ('calibre',10,'normal'))
        self.e1.place(x = 150, y = 50,height=22, width=140)
        self.e1.config(bg="#35363a",fg="white") 


        self.e2 = Entry(master,font = ('calibre',10,'normal')) 
        self.e2.place(x = 150, y = 100 ,height=22, width=140)
        self.e2.config(bg="#35363a",fg="white") 

        self.e3 = Entry(master,font = ('calibre',10,'normal')) 
        self.e3.place(x = 150, y = 150 ,height=22, width=140)
        self.e3.config(bg="#35363a",fg="white") 

        self.e4 = Entry(master,font = ('calibre',10,'normal')) 
        self.e4.place(x = 150, y = 200 ,height=22, width=140)
        self.e4.config(bg="#35363a",fg="white")

        #Button
        self.mybutton =Button(master,text="Submit",command=self.submit,activebackground = "black", activeforeground = "white")
        self.mybutton.place(x=110,y=250)
        self.mybutton.config(height=2,width=20)

    def submit(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        db="test"
        )
        c=mydb.cursor()
      
        sql = "INSERT INTO courier (sendername,senderadress,name,rollno) values(%s,%s,%s,%s)"
        val = (self.e1.get(), self.e2.get(), self.e3.get(),self.e4.get())
        c.execute(sql,val)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("","Datas Inserted")
        
    

a=App(top)
top.resizable(0,0)
mydb.commit()
mydb.close()
top.mainloop()