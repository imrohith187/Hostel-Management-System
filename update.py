from tkinter import *;
from tkinter import messagebox
import sys
top=Tk()
top.geometry("600x500")
top.title("Update")
class App:
    def __init__(self,master):
        myFrame=Frame(master)
        myFrame.pack()
        master.configure(background='#28282B')
        # master.configure(bg='yellow')

        #Button

        self.mybutton =Button(master,text="Student Info",command=self.student_info,fg='white', bg='#308d46')
        self.mybutton.place(x=180,y=80)
        self.mybutton.config(height=3,width=30)

        self.mybutton1 =Button(master,text="Room Info",command=self.room_info,fg='white', bg='#308d46')
        self.mybutton1.place(x=180,y=160)
        self.mybutton1.config(height=3,width=30)

        self.mybutton2 =Button(master,text="Mess Info",command=self.mess_info,fg='white', bg='#308d46')
        self.mybutton2.place(x=180,y=240)
        self.mybutton2.config(height=3,width=30)

        self.mybutton4 =Button(master,text="Complaint",command=self.complaint,fg='white', bg='#308d46')
        self.mybutton4.place(x=180,y=330)
        self.mybutton4.config(height=3,width=30)
        def on_enter(e):
            self.mybutton.config(background='#245e32', foreground= "white")
            
        def on_leave(e):
            self.mybutton.config(background= '#308d46', foreground= 'white')

        def on_enter1(e):
            self.mybutton1.config(background='#245e32', foreground= "white")
    
        def on_leave1(e):
            self.mybutton1.config(background= '#308d46', foreground= 'white')

        def on_enter2(e):
            self.mybutton2.config(background='#245e32', foreground= "white")
    
        def on_leave2(e):
            self.mybutton2.config(background= '#308d46', foreground= 'white')

        def on_enter4(e):
            self.mybutton4.config(background='#245e32', foreground= "white")
    
        def on_leave4(e):
            self.mybutton4.config(background= '#308d46', foreground= 'white')



        #Bind the Enter and Leave Events to the Button
        self.mybutton.bind('<Enter>', on_enter)
        self.mybutton.bind('<Leave>', on_leave)

        self.mybutton1.bind('<Enter>', on_enter1)
        self.mybutton1.bind('<Leave>', on_leave1)

        self.mybutton2.bind('<Enter>', on_enter2)
        self.mybutton2.bind('<Leave>', on_leave2)

        self.mybutton4.bind('<Enter>', on_enter4)
        self.mybutton4.bind('<Leave>', on_leave4)  

    def student_info(self):
        import updatestudent_info
        sys.modules.pop('student_infoupdate')
    def room_info(self):
        import updateroom_info
        sys.modules.pop('room_infoupdate')
    
    def mess_info(self):
        import updatemess
        sys.modules.pop('messupdate')

    def complaint(self):
        import updatecomplaints
        sys.modules.pop('updatecomplaints')
    

a=App(top)
top.resizable(0,0)
top.mainloop()