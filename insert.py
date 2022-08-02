from tkinter import *;
import sys
from tkinter import messagebox
top1=Tk()
top1.geometry("600x500")
top1.title("insert")
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

        self.mybutton2 =Button(master,text="Student sharing",command=self.student_sharing,fg='white', bg='#308d46')
        self.mybutton2.place(x=180,y=240)

        self.mybutton2.config(height=3,width=30)

        self.mybutton3 =Button(master,text="Mess",command=self.mess,fg='white', bg='#308d46')
        self.mybutton3.place(x=180,y=320)
        self.mybutton3.config(height=3,width=30)

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

        def on_enter3(e):
            self.mybutton3.config(background='#245e32', foreground= "white")
    
        def on_leave3(e):
            self.mybutton3.config(background= '#308d46', foreground= 'white')


        #Bind the Enter and Leave Events to the Button
        self.mybutton.bind('<Enter>', on_enter)
        self.mybutton.bind('<Leave>', on_leave)

        self.mybutton1.bind('<Enter>', on_enter1)
        self.mybutton1.bind('<Leave>', on_leave1)

        self.mybutton2.bind('<Enter>', on_enter2)
        self.mybutton2.bind('<Leave>', on_leave2)

        self.mybutton3.bind('<Enter>', on_enter3)
        self.mybutton3.bind('<Leave>', on_leave3)  

    def student_info(self):
        import insertstudent_info
        sys.modules.pop('student_info')
    
    def room_info(self):
        import insertroom_info
        sys.modules.pop('room_info')
    
    def student_sharing(self):
        import insertstudent_sharing
        sys.modules.pop('student_sharing')
    
    def mess(self):
        import insertmess
        sys.modules.pop('mess')
    

a=App(top1)
        
top1.resizable(0,0)
top1.mainloop()