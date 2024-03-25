from tkinter import *
from PIL import Image,ImageTk
from random import randint

def mainpart():
    #STEP 12. global variable set up
    remain=10
    user="User"


    #STEP 1. main window 
    root=Tk()
    root.title("Game page:Rock Paper Scissor")
    root.configure(background="#FFED93")

    #STEP 9. HEADING LINE
    hd=Label(root,text="Rock Paper Scissor Game \n Let us Play",font=('Times',50),fg="#1939d2",bg="#18FFFD").pack(pady=10)
    #STEP 4. frame
    f=Frame(root)
    f.configure(background="yellow")
    f.pack(expand=True,pady=0)


    #STEP 2. Computer and User and Vs Pic
    computer_img=ImageTk.PhotoImage(Image.open("COMPUTER.png"))
    user_img=ImageTk.PhotoImage(Image.open("USER.png"))
    vs_img=ImageTk.PhotoImage(Image.open("VS.png"))

    #STEP 3. PICTURE OF ROCK PAPER SCISSOR
    rock_img=ImageTk.PhotoImage(Image.open("USER ROCK .png"))
    paper_img=ImageTk.PhotoImage(Image.open("USER PAPER.png"))
    scissor_img=ImageTk.PhotoImage(Image.open("USER SCISSOR.png"))

    user_default_img=ImageTk.PhotoImage(Image.open("USER QUESTION MARK.png"))
    
    rock_img_comp=ImageTk.PhotoImage(Image.open("COMPUTER ROCK.png"))
    paper_img_comp=ImageTk.PhotoImage(Image.open("COMPUTER PAPER.png"))
    scissor_img_comp=ImageTk.PhotoImage(Image.open("COMPUTER SCISSOR.png"))

    comp_default_img=ImageTk.PhotoImage(Image.open("COMPUTER QUESTION MARK.png"))

    #STEP 5. DEFAULT PIC
    user_lb=Label(f,image=user_default_img,bg="#09568e")
    computer_lb=Label(f,image=comp_default_img,bg="#09568e")
    user_lb.grid(row=4,column=10)
    computer_lb.grid(row=4,column=1)




    #STEP 7. USER AND COMPUTER BOT AND Vs PIC
    user_pic=Label(f,image=user_img,bg="#09568e")
    computer_pic=Label(f,image=computer_img,bg="#09568e")
    vs_pic=Label(f,image=vs_img,bg="#09568e")
    user_pic.grid(row=0,column=10)
    vs_pic.grid(row=0,column=5)
    computer_pic.grid(row=0,column=1)

    #STEP 8. USER AND COMPUTER NAME LABEL
    computer_label=Label(f,text="COMPUTER",font=('Times',50),fg="#1939d2",bg="#18FFFD")
    user_label=Label(f,text=user,font=('Times',50),fg="#1939d2",bg="#18FFFD")
    user_label.grid(row=1,column=10)
    computer_label.grid(row=1,column=1)

    #STEP 10. Score label
    computer_score=Label(f,text="Score= 0",font=('Times',30),fg="#F26F2C",bg="#FFFFFF")
    user_score=Label(f,text="Score= 0",font=('Times',30),fg="#088948",bg="#FFFFFF")
    remain_time=Label(f,text="Remain_turn= 15",font=('Times',30),fg="#088948",bg="#FFFFFF")

    user_score.grid(row=2,column=10)
    remain_time.grid(row=1,column=5)
    computer_score.grid(row=2,column=1)

    #STEP 11. Button AND LABEL
    button_label=Label(f,text="User Button Select=",font=('Times',30),fg="#552386",bg="#FFE0EB").grid(row=5,column=5)
    rock=Button(f,width=10,height=2,text="Rock",fg='#D3434A',bg="#D0C1A7",font=('Times',20),command=lambda:updatechoices("rock")).grid(row=6,column=1)
    paper=Button(f,width=10,height=2,text="Paper",fg='#060708',bg="#FFFFFF",font=('Times',20),command=lambda:updatechoices("paper")).grid(row=6,column=5)
    scissor=Button(f,width=10,height=2,text="Scissor",fg='#060708',bg="#C3C1C2",font=('Times',20),command=lambda:updatechoices("scissor")).grid(row=6,column=10)

    #STEP 13. "AVAILABLE CHOICES"
    available_choices=["rock","paper","scissor"]

    #STEP 15. MAKE THE COMPUTER SCORE "+"
    def computer_score_update():
        val=computer_score["text"]
        val=int(val[6:])
        val+=1
        computer_score["text"]="Score= "+str(val)

    #STEP 16. MAKE THE USER SCORE "+"
    def user_score_update():
        val=user_score["text"]
        val=int(val[6:])
        val+=1
        user_score["text"]="Score= "+str(val)


    #STEP 17. "Evaluate" comp and user
    def evalmarks(user,comp):
        if user==comp:
            return
        elif user=="paper":
            if comp=="rock":
                user_score_update()
            else:
                computer_score_update()
        elif user=="rock":
            if comp=="scissor":
                user_score_update()
            else:
                computer_score_update()
        elif user=="scissor":
            if comp=="paper":
                user_score_update()
            else:
                computer_score_update()

    #STEP 18. "REMAIN" UPDATE
    def remain_update():
        val=remain_time["text"]
        val=int(val[12:])
        val-=1
        remain_time["text"]="Remain_turn= "+str(val)
        if(val==0):
            val1=user_score["text"]
            val1=int(val1[6:])
            val2=computer_score["text"]
            val2=int(val2[6:])
            root.destroy()
            resultsection(val1,val2)


    #STEP 14. "UPDATE CHOICES"
    def updatechoices(x):
        if x=="rock":
            user_lb.configure(image=rock_img)
        elif x=="paper":
            user_lb.configure(image=paper_img)
        else:
            user_lb.configure(image=scissor_img)

        com_choice_maker=available_choices[randint(0,2)]
        print(com_choice_maker ,"Vs",x,"(user)")
        if com_choice_maker=="rock":
            computer_lb.configure(image=rock_img_comp)
        elif com_choice_maker=="paper":
            computer_lb.configure(image=paper_img_comp)
        else:
            computer_lb.configure(image=scissor_img_comp)
        #evaluate
        evalmarks(x,com_choice_maker)
        remain_update()






    #STEP 6. ADD PADDING IN CHILDERN OF FRAME
    for child in f.winfo_children():
        child.grid_configure(padx=80,pady=10)

    root.mainloop()





def resultsection(user,comp):
    #Result Main Window
    root1=Tk()
    root1.title("Game Result:Rock Paper Scissor")
    root1.configure(background="#62CEC8")
    #Heading window
    hd1=Label(root1,text="Rock Paper Scissor Game \n Here Is The Result",font=('Times',50),fg="#1939d2",bg="#FFED93").pack(pady=1)

    #nessesary photo for result
    draw_img=ImageTk.PhotoImage(Image.open("YOU DRAW.png"))
    win_img=ImageTk.PhotoImage(Image.open("YOU WIN.png"))
    lose_img=ImageTk.PhotoImage(Image.open("YOU LOSE.png"))

    
    #messege declaration part
    if user==comp:
        result_pic=Label(root1,image=draw_img,bg="#09568e").pack()
        result_lb=Label(root1,text="It's a Draw!\n ''Peace?' said Vetinari. 'Ah, yes, defined as period of time to allow for preparation for the next war.'~Terry Pratchett",font=('Times',30),fg="#36566F",bg="#E0D4E8").pack()
    elif user>comp:
        result_pic=Label(root1,image=win_img,bg="#09568e").pack()
        result_lb=Label(root1,text="Hurray!You Win The Match.\n “The harder the battle, the sweeter the victory.” – Les Brown (2012)",font=('Times',30),fg="#34944A",bg="#E0D4E8").pack()
    else:
        result_pic=Label(root1,image=lose_img,bg="#09568e").pack()
        result_lb=Label(root1,text="Sorry!You lose The Match.\n “Failure is simply the opportunity to begin again, this time more intelligently.” – Henry Ford (1947)",font=('Times',30),fg="#A80119",bg="#E0D4E8").pack()
        

     #frame1
    f1=Frame(root1)
    f1.configure(background="#CDEDFF")
    f1.pack(expand=True,pady=0)
    f2=Frame(f1)
    #Frame2 in frame1
    f2.configure(background="#CDEDFF")
    f2.pack(expand=True)

    #labels in Frame 2
    computer_score1=Label(f2,text="Computer Score",font=('Times',30),fg="#561C67",bg="#EDC9CA")
    user_score1=Label(f2,text="User Score",font=('Times',30),fg="#5A4231",bg="#EFE4B3")
    user_score1.grid(row=0,column=10)
    computer_score1.grid(row=0,column=1)
    computer_score1_print=Label(f2,text=comp,font=('Times',30),fg="#392A86",bg="#BDEFDE")
    user_score1_print=Label(f2,text=user,font=('Times',30),fg="#272727",bg="#DBDBDB")
    user_score1_print.grid(row=1,column=10)
    computer_score1_print.grid(row=1,column=1)

    
    
    

    #Replay Button Function
    def gotomainpart():
        root1.destroy()
        mainpart()


    #restart and exit button
    Exit=Button(f2,width=10,height=2,text="Exit",fg='#C62940',bg="#F8EBD8",font=('Times',20),command=lambda:root1.destroy()).grid(row=2,column=1)
    Replay=Button(f2,width=10,height=2,text="Replay",fg='#060708',bg="#C0C86F",font=('Times',20),command=lambda:gotomainpart()).grid(row=2,column=10)

    #add padding in the children of Frame 2
    for child in f2.winfo_children():
            child.grid_configure(padx=80,pady=10)

    root1.mainloop()
mainpart()

