from tkinter import *;
import tkinter.font as font 
import sys
from tkinter import messagebox
top=Tk()
top.geometry("600x500")
top.title("Main")
class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()
        master.configure(background='#28282B')

        #font 
        # self.myFont = font.Font(family='Helvetica', size=8, weight='bold')
        # buttoninsert
        self.insert=Button(master,text="Insert",command=self.clickinsert,fg='white', bg='#308d46')
        self.insert.place(x=200,y=80)
        self.insert.config(height=3,width=30)

        self.view=Button(master,text="View",command=self.clickview,fg='white', bg='#308d46')
        self.view.place(x=200,y=180)
        self.view.config(height=3,width=30)

        self.update=Button(master,text="Update",command=self.clickupdate,fg='white', bg='#308d46')
        self.update.place(x=200,y=280)
        self.update.config(height=3,width=30)

        self.insertcourier=Button(master,text="Insert Courier",command=self.clickcourier,fg='white', bg='#308d46')
        self.insertcourier.place(x=45,y=380)
        self.insertcourier.config(height=3,width=30)

        self.complaints=Button(master,text="View Complaints",command=self.clickcomplaint,fg='white', bg='#308d46')
        self.complaints.place(x=320,y=380)
        self.complaints.config(height=3,width=30)


        def on_enter(e):
            self.insert.config(background='#245e32', foreground= "white")
            
        def on_leave(e):
            self.insert.config(background= '#308d46', foreground= 'white')

        def on_enter1(e):
            self.view.config(background='#245e32', foreground= "white")
    
        def on_leave1(e):
            self.view.config(background= '#308d46', foreground= 'white')

        def on_enter2(e):
            self.update.config(background='#245e32', foreground= "white")
    
        def on_leave2(e):
            self.update.config(background= '#308d46', foreground= 'white')

        def on_enter3(e):
            self.insertcourier.config(background='#245e32', foreground= "white")
    
        def on_leave3(e):
            self.insertcourier.config(background= '#308d46', foreground= 'white')

        def on_enter4(e):
            self.complaints.config(background='#245e32', foreground= "white")
    
        def on_leave4(e):
            self.complaints.config(background= '#308d46', foreground= 'white')

    #Bind the Enter and Leave Events to the Button
        self.insert.bind('<Enter>', on_enter)
        self.insert.bind('<Leave>', on_leave)

        self.view.bind('<Enter>', on_enter1)
        self.view.bind('<Leave>', on_leave1)

        self.update.bind('<Enter>', on_enter2)
        self.update.bind('<Leave>', on_leave2)

        self.insertcourier.bind('<Enter>', on_enter3)
        self.insertcourier.bind('<Leave>', on_leave3)

        self.complaints.bind('<Enter>', on_enter4)
        self.complaints.bind('<Leave>', on_leave4)
        #Create a Button

    def clickinsert(self):
        import insert
        sys.modules.pop('insert')

    def clickview(self):
        import view
        sys.modules.pop('view')
    def clickupdate(self):
        import update
        sys.modules.pop('update')
    def clickcourier(self):
        import insertcourier
        sys.modules.pop('insertcourier')
    def clickcomplaint(self):
        import viewcomplaint
        sys.modules.pop('viewcomplaint')
a=App(top)
top.resizable(0,0)
top.mainloop()
