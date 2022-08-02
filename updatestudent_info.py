from tkinter import *;
from tkinter import messagebox
import mysql.connector
top=Tk()
top.geometry("450x500")
top.title("Student Info")
class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()
        master.configure(background='#28282B')
         #lables

        self.Rollno = Label(master, text = "Rollno",font = ("Arial", 11))
        self.Rollno .place(x = 25, y = 50)
        self.Rollno.config(bg="#28282B",fg="white")  

        self.Email = Label(master, text = "Email",font = ("Arial", 11))
        self.Email.place(x = 25,y = 100) 
        self.Email.config(bg="#28282B",fg="white")   
         
        self.Pin = Label(master, text = "PNO",font = ("Arial", 11))
        self.Pin .place(x = 25, y = 150) 
        self.Pin.config(bg="#28282B",fg="white")  

        #entities
        self.e2 = Entry(master,font = ('calibre',10,'normal')) 
        self.e2.place(x = 110, y = 50 ,height=22, width=140)

        self.e5 = Entry(master,font = ('calibre',10,'normal')) 
        self.e5.place(x = 110, y = 100 ,height=22, width=140)

        self.e6 = Entry(master,font = ('calibre',10,'normal')) 
        self.e6.place(x = 110, y = 150 ,height=22, width=140)        

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
        sql= "UPDATE student_info set email=%s,phoneno=%s where rollno=%s"
        val=(self.e5.get(),self.e6.get(),self.e2.get())
        c.execute(sql,val)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("","Datas Updated") 

    
    

a=App(top)
top.resizable(0,0)
top.mainloop()