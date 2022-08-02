from tkinter import *;
from tkinter import messagebox
import mysql.connector

top=Tk()
top.geometry("450x500")
top.title("EHostel")

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

        self.roomtype = Label(master, text = "Login",font = ("Arial", 20))
        self.roomtype.place(x = 25,y = 125)
        self.roomtype.config(bg="#28282B",fg="white") 
         

        #entities

        self.R1 = Radiobutton(top, text="Student", variable=self.radio, value=1,font="Arial",width=10)  
        self.R1.place(x=150,y=100)  

        self.R2 = Radiobutton(top, text="Admin Login", variable=self.radio, value=2,font="Arial",width=10)  
        self.R2.place(x=150,y=150)  
        #Button

        self.mybutton =Button(master,text="Proceed",command=self.submit,activebackground = "black", activeforeground = "white",font="Arial")
        self.mybutton.place(x=110,y=230)
        self.mybutton.config(height=1,width=20)

    def submit(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        db="test"
        )
        c=mydb.cursor()

        if(self.radio.get() ==1):
            top.destroy()
            import fourth
        elif(self.radio.get() ==2):
            top.destroy()
            import second
        
    

a=App(top)
top.resizable(0,0)
mydb.commit()
mydb.close()
top.mainloop()