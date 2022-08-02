from tkinter import *;
from tkinter import messagebox
import sys
top=Tk()
top.geometry("600x500")
top.title("Student Window")
class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()
        master.configure(background='#28282B')
        # master.configure(bg='yellow')

        #Button

        self.mybutton =Button(master,text="View Courier",command=self.courier,fg='white', bg='#308d46')
        self.mybutton.place(x=180,y=160)
        self.mybutton.config(height=3,width=30)

        self.mybutton1 =Button(master,text="Insert Complaint",command=self.complaint,fg='white', bg='#308d46')
        self.mybutton1.place(x=180,y=240)
        self.mybutton1.config(height=3,width=30)

        def on_enter1(e):
            self.mybutton.config(background='#245e32', foreground= "white")
    
        def on_leave1(e):
            self.mybutton.config(background= '#308d46', foreground= 'white')

        def on_enter2(e):
            self.mybutton1.config(background='#245e32', foreground= "white")
    
        def on_leave2(e):
            self.mybutton1.config(background= '#308d46', foreground= 'white')



        #Bind the Enter and Leave Events to the Button

        self.mybutton.bind('<Enter>', on_enter1)
        self.mybutton.bind('<Leave>', on_leave1)

        self.mybutton1.bind('<Enter>', on_enter2)
        self.mybutton1.bind('<Leave>', on_leave2)

    def courier(self):
        import viewcourier
        sys.modules.pop('viewcourier')
    def complaint(self):
        import insertcomplaint
        sys.modules.pop('insertcomplaint')
    

a=App(top)
top.resizable(0,0)
top.mainloop()