from tkinter import *
from tkinter import messagebox

top=Tk()
top.geometry("300x200")
top.title("Login")
class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()
        master.configure(background='#28282B')

        #lables
        self.Login = Label(master, text = "UserName",font = ("Arial", 11))
        self.Login.place(x = 25,y = 50)   
        self.password = Label(master, text = "Password",font = ("Arial", 11))
        self.password .place(x = 25, y = 100)  
        #entities
        self.e1 = Entry(master,font = ('calibre',10,'normal'))
        self.e1.place(x = 110, y = 50,height=22, width=140)    
        self.e3 = Entry(master,font = ('calibre',10,'normal'), show = '*') 
        self.e3.place(x = 110, y = 100 ,height=22, width=140)

        self.mybutton =Button(master,text="Login",command=self.click,activebackground = "black", activeforeground = "white")
        self.mybutton.place(x=100,y=150)
        self.mybutton.config(height=1,width=8)

    def click(self):
        username=self.e1.get()
        password=self.e3.get()

        if(username=="Admin" and password=="1234"):
            messagebox.showinfo("","Login Successfull")
            top.destroy()
            import third

        elif(username=="" and password==""):
            messagebox.showinfo("","Enter Valid Input")
        else:
            messagebox.showinfo("","incorrect username and password")
    

a=App(top)
top.resizable(0,0)
top.mainloop()


