
from tkinter import *
import pytz
import time
from datetime import datetime
from PIL import ImageTk,Image
root=Tk()
root.geometry("1000x800")
root.title("World Clock")
aus_img=ImageTk.PhotoImage(Image.open("aus.png"))
usa_img=ImageTk.PhotoImage(Image.open("usa.png"))
ind_img=ImageTk.PhotoImage(Image.open("ind.png"))
jpn_img=ImageTk.PhotoImage(Image.open("jpn.png"))

IND_LBL=Label(root,text="INDIA")
IND_LBL.place(relx=0.2,rely=0.05,anchor=CENTER)
IND_time=Label(root,image=ind_img)
IND_time.place(relx=0.2,rely=0.2,anchor=CENTER)
IND_HOUR=Label(root)
IND_HOUR.place(relx=0.2, rely=0.35,anchor=CENTER)

class India():
    def times(self):
        home= pytz.timezone('Asia/Kolkata')
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%H:%M:%S")
        IND_HOUR["text"]="time: "+currenttime
        IND_HOUR.after(200,self.times)
        
USA_LBL=Label(root,text="USA")
USA_LBL.place(relx=0.7,rely=0.05,anchor=CENTER)
USA_time=Label(root,image=usa_img)
USA_time.place(relx=0.7,rely=0.2,anchor=CENTER)
USA_HOUR=Label(root)
USA_HOUR.place(relx=0.7, rely=0.35,anchor=CENTER)   
     
class USA():
    def times(self):
        home= pytz.timezone('US/Central')
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%H:%M:%S")
        USA_HOUR["text"]="time: "+currenttime
        USA_HOUR.after(200,self.times)
        
objIND=India()  
ind_btn=Button(root,text="Show time",command=objIND.times)
ind_btn.place(relx=0.2, rely=0.4,anchor=CENTER)

objUSA=USA()
usa_btn=Button(root,text="Show time",command=objUSA.times)
usa_btn.place(relx=0.7, rely=0.4,anchor=CENTER)

aus_LBL=Label(root,text="Australia")
aus_LBL.place(relx=0.2,rely=0.5,anchor=CENTER)
aus_time=Label(root,image=aus_img)
aus_time.place(relx=0.2,rely=0.65,anchor=CENTER)
aus_HOUR=Label(root)
aus_HOUR.place(relx=0.2, rely=0.8,anchor=CENTER)

class aus():
    def times(self):
        home= pytz.timezone('Australia/ACT')
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%H:%M:%S")
        aus_HOUR["text"]="time: "+currenttime
        aus_HOUR.after(200,self.times)
        
jpn_LBL=Label(root,text="Japan")
jpn_LBL.place(relx=0.7,rely=0.5,anchor=CENTER)
jpn_time=Label(root,image=jpn_img)
jpn_time.place(relx=0.7,rely=0.65,anchor=CENTER)
jpn_HOUR=Label(root)
jpn_HOUR.place(relx=0.7, rely=0.8,anchor=CENTER)   
     
class jpn():
    def times(self):
        home= pytz.timezone('Japan')
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%H:%M:%S")
        jpn_HOUR["text"]="time: "+currenttime
        jpn_HOUR.after(200,self.times)
        
objaus=aus()  
aus_btn=Button(root,text="Show time",command=objaus.times)
aus_btn.place(relx=0.2, rely=0.9,anchor=CENTER)

objjpn=jpn()
jpn_btn=Button(root,text="Show time",command=objjpn.times)
jpn_btn.place(relx=0.7, rely=0.9,anchor=CENTER) 
        
root.mainloop()