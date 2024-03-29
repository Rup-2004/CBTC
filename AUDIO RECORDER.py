



from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from scipy.io.wavfile import write
import sounddevice as sdd
import time

custom_time_storer=int()

def recorder(time1):
    
    root5=Tk()
    root5.title("Main page: Rupayan Audio Recorder")
    root5.configure(background="#11C5EF")
    root5.geometry("300x700")
    hd=Label(root5,text="Welcome\n \nRecording Started.\n\n Remaining time",font=('Times',20),fg="#1939d2",bg="#11C5EF").pack(pady=5)
    recorder_img=ImageTk.PhotoImage(Image.open("MIC.png"))
    recorder_pic=Label(root5,image=recorder_img,bg="#09568e").pack()
    freq=44100
    a=time1*freq
    record=sdd.rec(a,samplerate=freq,channels=2)

    digitcounter=len(str(time1))

    def adjust(p,n):                #digit of timer adjusting part
        p=str(p)
        if len(p)==n:
            return p
        else:
            return ("0"*(n-len(p)))+p
    

    temp=time1
    while temp>0:                                                           #timer part start with remaining time
        root5.update()
        time.sleep(1)
        temp-=1
        mytext=adjust(temp,digitcounter)

        Label(text=mytext,font=('Times',60),fg="#1939d2",bg="#11C5EF").place(x=130,y=500)
        if (temp==0):
            root5.destroy()                                                     #timer part end with exit from thos page



    
    sdd.wait()
    n=str(time.time())
    name=n+".wav"
    write(name,freq,record)
    messagebox.showinfo("recording status",name+" is recorded successfully.Please note the name of file.\n\nThanks from Rupayan Ghosh for using this.")
    buttonselectpage()
    root5.mainloop()




def buttonselectpage():
    #STEP 1. main window 
    root=Tk()
    root.title("Main page: Rupayan Audio Recorder")
    root.configure(background="#11C5EF")
    root.geometry("300x700")
    hd=Label(root,text="Welcome\n to\nRG_Studio",font=('Times',20),fg="#1939d2",bg="#11C5EF").pack(pady=5)
    recorder_img=ImageTk.PhotoImage(Image.open("MIC.png"))
    recorder_pic=Label(root,image=recorder_img,bg="#09568e").pack()
    button_label=Label(root,text="select the time=",font=('Times',20),fg="#552386",bg="#FFE0EB").pack(pady=10)
    f=Frame(root)
    f.configure(background="yellow")
    f.pack(expand=True,pady=0)
    
    onemin=Button(f,width=10,height=2,text="1 min",fg='#ECECEC',bg="#3D84C2",font=('Times',15),command=lambda:fixedmin_function(1)).grid(row=2,column=1)
    fivemin=Button(f,width=10,height=2,text="5 min",fg='#ECECEC',bg="#59B359",font=('Times',15),command=lambda:fixedmin_function(5)).grid(row=2,column=5)
    tenmin=Button(f,width=10,height=2,text="10 min",fg='#ECECEC',bg="#EB9A24",font=('Times',15),command=lambda:fixedmin_function(10)).grid(row=3,column=1)
    fifteenmin=Button(f,width=10,height=2,text="15 min",fg='#ECECEC',bg="#34B0D4",font=('Times',15),command=lambda:fixedmin_function(15)).grid(row=3,column=5)
    thirtymin=Button(f,width=10,height=2,text="30 min",fg='#89050A',bg="#FFF8DD",font=('Times',15),command=lambda:fixedmin_function(30)).grid(row=4,column=1)
    custommin=Button(f,width=10,height=2,text="CUSTOM\nmin",fg='#ECECEC',bg="#80329B",font=('Times',15),command=lambda:custommin_function()).grid(row=4,column=5)
    exitroot=Button(root,width=10,height=2,text="exit",fg='#FFF8DD',bg="#89050A",font=('Times',15),command=lambda:exitpls()).pack(pady=10)
    
    for child in f.winfo_children():
        child.grid_configure(padx=7,pady=3)

    def custommin_function():
        root.destroy()                                                      #exit and goto custom value taking page page
        custompage()
    def fixedmin_function(timeint):
        root.destroy()
        recordingpage(timeint*60)                       #exit and goto recording button page
    def exitpls():
        root.destroy()

    root.mainloop()










def custompage():
    global custom_time_storer
    #STEP 1. main window 
    root3=Tk()
    root3.title("Custom Time page: Rupayan Audio Recorder")
    root3.configure(background="#11C5EF")
    root3.geometry("300x600")

    #tkinter IntVar variable
    cust_time=IntVar(root3)
    hd3=Label(root3,text="Recorder",font=('Times',20),fg="#1939d2",bg="#11C5EF").pack(pady=5)
    recorder_img3=ImageTk.PhotoImage(Image.open("C:/Users/INTEL/OneDrive/INTERNSHIP ON AUDIO RECOEDER USING SOUNDDEVICE/MIC2.png"))
    recorder_pic=Label(root3,image=recorder_img3,bg="#09568e").pack()
    button_label=Label(root3,text="Write the time in sec.=",font=('Times',20),fg="#552386",bg="#FFE0EB").pack(pady=10)
    entry_part=Entry(root3,textvariable=cust_time,font=('Times',30),bg='#FAFFBD',width=5).pack()
    recorder=Button(root3,width=10,height=2,text="Submit",fg='#ECECEC',bg="#80329B",font=('Times',15),command=lambda:submit()).pack(pady=10)
    exitroot=Button(root3,width=10,height=2,text="back",fg='#FFF8DD',bg="#89050A",font=('Times',15),command=lambda:exitpls()).pack(pady=10)


    def submit():
        custom_time_storer=cust_time.get()
        root3.destroy()                     #exit and goto recording button page
        recordingpage(custom_time_storer)

    def exitpls():
        root3.destroy()
        buttonselectpage()      #exit and goto main page
        
    
    root3.mainloop()



def recordingpage(a):
    #STEP 1. main window
    global custom_time_storer
    custom_time_storer=a
    root2=Tk()
    root2.title(" Recording page: Rupayan Audio Recorder")
    root2.configure(background="#11C5EF")
    root2.geometry("300x600")
    hd2=Label(root2,text="Recorder",font=('Times',20),fg="#1939d2",bg="#11C5EF").pack(pady=5)
    recorder_img2=ImageTk.PhotoImage(Image.open("C:/Users/INTEL/OneDrive/INTERNSHIP ON AUDIO RECOEDER USING SOUNDDEVICE/MIC2.png"))
    recorder_pic=Label(root2,image=recorder_img2,bg="#09568e").pack()
    label2=Label(root2,text="Press Record Button to \nstart Recording.",font=('Times',20),fg="#552386",bg="#FFE0EB").pack(pady=10)
    backprevious_page=Button(root2,width=10,height=2,text="Record",fg='#ECECEC',bg="#80329B",font=('Times',15),command=lambda:isrec()).pack(pady=10)
    exitroot=Button(root2,width=10,height=2,text="Back",fg='#FFF8DD',bg="#89050A",font=('Times',15),command=lambda:exitpls()).pack(pady=10)


    def isrec():
        root2.destroy()
        recorder(custom_time_storer)        #goto recorder part
        
    def exitpls():
        
        root2.destroy()
        buttonselectpage()                  #exit and goto main page
        
        
    
    
    root2.mainloop()

buttonselectpage()


