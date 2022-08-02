from tkinter import *;
from tkinter import messagebox
import mysql.connector
top=Tk()
top.geometry("450x500")
top.title("Mess")

class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()
        master.configure(background='#28282B')
        # master.configure(bg='yellow')
        #values
        self.radio = IntVar()  
        self.radio1=IntVar()

         #lables
        self.Rollno = Label(master, text = "Rollno",font = ("Arial", 11))
        self.Rollno.place(x = 25,y = 50)  

        self.block = Label(master, text = "Food",font = ("Arial", 11))
        self.block.place(x = 25,y = 100)  

        self.roomtype = Label(master, text = "Food Type",font = ("Arial", 11))
        self.roomtype.place(x = 25,y = 170) 
         

        #entities
        self.e1 = Entry(master,font = ('calibre',10,'normal'))
        self.e1.place(x = 110, y = 50,height=22, width=140)

        self.R1 = Radiobutton(master, text="Veg", variable=self.radio, value=1)  
        self.R1.place(x=110,y=100)  

        self.R2 = Radiobutton(master, text="Non-Veg", variable=self.radio, value=2)  
        self.R2.place(x=110,y=120)  

        self.R3 = Radiobutton(master, text="South Indian", variable=self.radio1, value=1)  
        self.R3.place(x=110,y=170)  

        self.R4 = Radiobutton(master, text="North Indian", variable=self.radio1, value=2)  
        self.R4.place(x=110,y=190)  

        #Button

        self.mybutton =Button(master,text="Submit",command=self.submit,activebackground = "black", activeforeground = "white")
        self.mybutton.place(x=110,y=260)
        self.mybutton.config(height=2,width=20)

    def submit(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        db="test"
        )
        if(self.radio.get()==1):
            a="Veg"
        elif(self.radio.get()==2):
            a="Non-Veg"

        if(self.radio1.get()==1):
            b="South Indian"
        elif(self.radio1.get()==2):
            b="North Indian"          

        c=mydb.cursor()

        sql = "UPDATE mess SET veg_nonveg=%s,menutype=%s WHERE rollno=%s"
        val = (self.e2.get(),a,b,self.e1.get())
        c.execute(sql,val)
        mydb.commit()
        mydb.close() 
        messagebox.showinfo("","Datas Updated")
    
    

a=App(top)
top.resizable(0,0)
top.mainloop()