from tkinter import *
from tkinter import messagebox
import mysql.connector
top=Tk()
top.geometry("450x500")
top.title("Student Info")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  db="test"
)

class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()
        master.configure(background='#28282B')
         #lables
         #values
        options = [
            "O+",
            "O-",
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-"
                ]
        self.clicked = StringVar()
        

        self.Name = Label(master, text = "Name",font = ("Arial", 11))
        self.Name.place(x = 25,y = 50)
        self.Name.config(bg="#28282B",fg="white")  

        self.Rollno = Label(master, text = "Rollno",font = ("Arial", 11))
        self.Rollno .place(x = 25, y = 100)
        self.Rollno.config(bg="#28282B",fg="white")   

        self.Age = Label(master, text = "Age",font = ("Arial", 11))
        self.Age.place(x = 25,y = 150)
        self.Age.config(bg="#28282B",fg="white")   
         
        self.Blood = Label(master, text = "Blood",font = ("Arial", 11))
        self.Blood .place(x = 25, y = 200)
        self.Blood.config(bg="#28282B",fg="white")   

        self.Email = Label(master, text = "Email",font = ("Arial", 11))
        self.Email.place(x = 25,y = 250) 
        self.Email.config(bg="#28282B",fg="white")   
         
        self.phone = Label(master, text = "Phoneno",font = ("Arial", 11))
        self.phone .place(x = 25, y = 300) 
        self.phone.config(bg="#28282B",fg="white")  

        #entities
        self.e1 = Entry(master,font = ('calibre',10,'normal'))
        self.e1.place(x = 110, y = 50,height=22, width=140)


        self.e2 = Entry(master,font = ('calibre',10,'normal')) 
        self.e2.place(x = 110, y = 100 ,height=22, width=140)

        self.e3 = Entry(master,font = ('calibre',10,'normal')) 
        self.e3.place(x = 110, y = 150 ,height=22, width=140)

        self.clicked.set( "None" )   
        self.drop = OptionMenu( master  ,self.clicked, *options )
        self.drop.place(x=110,y=200)

        self.e5 = Entry(master,font = ('calibre',10,'normal')) 
        self.e5.place(x = 110, y = 250 ,height=22, width=140)

        self.e6 = Entry(master,font = ('calibre',10,'normal')) 
        self.e6.place(x = 110, y = 300 ,height=22, width=140)        

        #Button

        self.mybutton =Button(master,text="Submit",command=self.submit,activebackground = "black", activeforeground = "white")
        self.mybutton.place(x=110,y=340)
        self.mybutton.config(height=2,width=20)

    def submit(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        db="test"
        )
        c=mydb.cursor()
        sql = "INSERT INTO student_info (name,rollno,age,bloodgroup,email,phoneno) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.e1.get(), self.e2.get(),self.e3.get(),self.clicked.get(),self.e5.get(),self.e6.get())
        c.execute(sql,val)
        mydb.commit()
        mydb.close() 
        messagebox.showinfo("","Datas Inserted")
    
    

a=App(top)
top.resizable(0,0)
mydb.commit()
mydb.close() 
top.mainloop()