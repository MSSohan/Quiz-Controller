import time
from tkinter import *
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


master = Tk()

width_value = master.winfo_screenwidth()
height_value = master.winfo_screenheight()


# width_value = 800
# height_value= 400

BigFont=  int(width_value/15)
SmallFont= int(height_value/30)
DiffHeight= int(height_value/8)
LeftGap = int(width_value/12)
BackgroundColor = "black"
FontColor = "white"


print(width_value,height_value)

master.geometry("%dx%d" % (width_value+0,height_value+ 0))
master.configure(bg="black")
master.wm_attributes("-fullscreen","True")

# master.mainloop()
# import tkinter as tk
# w = tk.Tk()
master.title('main')
# w.geometry('300x300')





Team1 = 11
Team2 = 12
Team3 = 13
Team4 = 15
Team5 = 16
Team6 = 18
reset = 22
buzzer= 24

GPIO.setup(Team1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team6,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(reset,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,GPIO.LOW)
# GPIO.output(buzzer,GPIO.HIGH)
def timeFunc():
    millis = lambda: ((time.time()*1000))


def test():
    li =[]
    millis = lambda: ((time.time()))
    Buzzer= False
    try:
        while True:  
            if GPIO.input(Team1)==0:
                if "Team1" not in li:
                    print("Team 1 was pressed")
                    li.append("Team1")
                    print(li)
            if GPIO.input(Team2)==0:
                if "Team2" not in li:
                    print("Team 2 was pressed")
                    li.append("Team2")
                    print(li)
            if GPIO.input(Team3)==0:
                if "Team3" not in li:
                    print("Team 3 was pressed")
                    li.append("Team3")
                    print(li)
            if GPIO.input(Team4)==0:
                if "Team4" not in li:
                    print("Team 4 was pressed")
                    li.append("Team4")
                    print(li)
            if GPIO.input(Team5)==0:
                if "Team5" not in li:
                    print("Team 5 was pressed")
                    li.append("Team5")
                    print(li)
            if GPIO.input(Team6)==0:
                if "Team6" not in li:
                    print("Team 6 was pressed")
                    li.append("Team6")
                    print(li)
            if GPIO.input(reset)==0:
                li=[]
                Sound = True
                Buzzer = False
                print(li)
            try:
                if len(li)>=1:
                    FirstRes['text'] = li[0]
                    mainFirst['text'] = li[0]
                else:
                    FirstRes['text'] = " "
                    mainFirst['text']= " READY!! "
                    
                if len(li)>=2:
                    SecondRes['text'] = li[1]
                else:
                    SecondRes['text'] = " "
                    
                if len(li)>=3:
                    ThirdRes['text'] = li[2]
                else:
                    ThirdRes['text'] = " "
                    
                if len(li)>=4:
                    FourthRes['text'] = li[3]
                else:
                    FourthRes['text'] = " "
                    
                if len(li)>=5:
                    FifthRes['text'] = li[4]
                else:
                    FifthRes['text'] = " "
                    
                if len(li)>=6:
                    SixthRes['text'] = li[5]
                else:
                    SixthRes['text'] = " "
                
                if len(li) == 1 and Buzzer == False:
                    GPIO.output(buzzer,GPIO.HIGH)
                    trigger = millis()
                    Buzzer = True
                print(trigger,millis())
                if Buzzer == True and (millis()-trigger) >= 1:
                    GPIO.output(buzzer,GPIO.LOW)
                    
                #else:
                   # GPIO.output(buzzer,GPIO.LOW)
            except:
                x=0
            
            master.update()
            
    except:
        print("error")



#     print(millis())
    

mainFirst = Label(master,font=("Roboto", BigFont),bg=BackgroundColor,fg=FontColor)

First = Label(master,text="1st:",font=("Helvetica", SmallFont,"bold" ),bg=BackgroundColor,fg=FontColor)
Second = Label(master,text="2nd:",font=("Helvetica", SmallFont,"bold"),bg=BackgroundColor,fg=FontColor)
Third = Label(master,text="3rd:",font=("Helvetica", SmallFont,"bold"),bg=BackgroundColor,fg=FontColor)
Fourth = Label(master,text="4th:",font=("Helvetica", SmallFont,"bold"),bg=BackgroundColor,fg=FontColor)
Fifth = Label(master,text="5th:",font=("Helvetica", SmallFont,"bold"),bg=BackgroundColor,fg=FontColor)
Sixth = Label(master,text="6th:",font=("Helvetica", SmallFont,"bold"),bg=BackgroundColor,fg=FontColor)   

FirstRes= Label(master,font=("Helvetica", SmallFont),bg=BackgroundColor,fg=FontColor)
SecondRes= Label(master,font=("Helvetica", SmallFont),bg=BackgroundColor,fg=FontColor)
ThirdRes= Label(master,font=("Helvetica", SmallFont),bg=BackgroundColor,fg=FontColor)
FourthRes= Label(master,font=("Helvetica", SmallFont),bg=BackgroundColor,fg=FontColor)
FifthRes= Label(master,font=("Helvetica", SmallFont),bg=BackgroundColor,fg=FontColor)
SixthRes= Label(master,font=("Helvetica", SmallFont),bg=BackgroundColor,fg=FontColor)

mainFirst.place(x=(width_value/4)-(BigFont*2), y=((height_value/2)-BigFont))

First.place(x=(width_value/4)+(width_value/2)-LeftGap, y=((height_value/2)-(DiffHeight*3)))
Second.place(x=(width_value/4)+(width_value/2)-LeftGap, y=((height_value/2)-(DiffHeight*2)))
Third.place(x=(width_value/4)+(width_value/2)-LeftGap, y=((height_value/2)-DiffHeight))
Fourth.place(x=(width_value/4)+(width_value/2)-LeftGap, y=((height_value/2)+0))
Fifth.place(x=(width_value/4)+(width_value/2)-LeftGap, y=((height_value/2)+(DiffHeight)))
Sixth.place(x=(width_value/4)+(width_value/2)-LeftGap, y=((height_value/2)+(DiffHeight*2)))

FirstRes.place(x=(width_value/4)+(width_value/2)-LeftGap+150, y=((height_value/2)-(DiffHeight*3)))
SecondRes.place(x=(width_value/4)+(width_value/2)-LeftGap+150, y=((height_value/2)-(DiffHeight*2)))
ThirdRes.place(x=(width_value/4)+(width_value/2)-LeftGap+150, y=((height_value/2)-DiffHeight))
FourthRes.place(x=(width_value/4)+(width_value/2)-LeftGap+150, y=((height_value/2)+0))
FifthRes.place(x=(width_value/4)+(width_value/2)-LeftGap+150, y=((height_value/2)+(DiffHeight)))
SixthRes.place(x=(width_value/4)+(width_value/2)-LeftGap+150, y=((height_value/2)+(DiffHeight*2)))

# First.place(x=0, y=0)
# Second.pack()
test()
mainloop()
