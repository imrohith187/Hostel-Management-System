from tkinter import *;
from tkinter import messagebox
import mysql.connector

top=Tk()
top.geometry("450x500")
top.title("Room Info")

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
        self.Rollno = Label(master, text = "Rollno",font = ("Arial", 11))
        self.Rollno.place(x = 25,y = 50)
        self.Rollno.config(bg="#28282B",fg="white")  

        self.Roomno = Label(master, text = "Roomno",font = ("Arial", 11))
        self.Roomno .place(x = 25, y = 100) 
        self.Roomno.config(bg="#28282B",fg="white") 

        self.block = Label(master, text = "Block",font = ("Arial", 11))
        self.block.place(x = 25,y = 150)
        self.block.config(bg="#28282B",fg="white") 

        self.roomtype = Label(master, text = "Room Type",font = ("Arial", 11))
        self.roomtype.place(x = 25,y = 200)
        self.roomtype.config(bg="#28282B",fg="white") 
         

        #entities
        self.e1 = Entry(master,font = ('calibre',10,'normal'))
        self.e1.place(x = 110, y = 50,height=22, width=140)
        self.e1.config(bg="#35363a",fg="white") 


        self.e2 = Entry(master,font = ('calibre',10,'normal')) 
        self.e2.place(x = 110, y = 100 ,height=22, width=140)
        self.e2.config(bg="#35363a",fg="white") 

        self.e3 = Entry(master,font = ('calibre',10,'normal')) 
        self.e3.place(x = 110, y = 150 ,height=22, width=140)
        self.e3.config(bg="#35363a",fg="white") 

        self.R1 = Radiobutton(top, text="2 sharing", variable=self.radio, value=1)  
        self.R1.place(x=110,y=200)  

        self.R2 = Radiobutton(top, text="4 sharing", variable=self.radio, value=2)  
        self.R2.place(x=110,y=220)  

        self.R3 = Radiobutton(top, text="6 sharing", variable=self.radio, value=3)  
        self.R3.place( x=110,y=240)
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

        if(self.radio.get() ==1):
          a="2 sharing"
        elif(self.radio.get() ==2):
          a="4 sharing"
        elif(self.radio.get() ==3):
          a="6 sharing"
      
        sql = "UPDATE room_info SET roomno=%s,block=%s,roomtype=%s WHERE rollno=%s"
        sql1= "UPDATE student_sharing SET roomno=%s,block=%s WHERE rollno=%s"
        val = (self.e2.get(), self.e3.get(), a, self.e1.get())
        val1 = (self.e2.get(), self.e3.get(), self.e1.get())
        c.execute(sql,val)
        c.execute(sql1,val1)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("","Datas Updated")
        
    

a=App(top)
top.resizable(0,0)
mydb.commit()
mydb.close()
top.mainloop()