from lib2to3.pgen2.token import LEFTSHIFT
from tkinter import *

from pip import main
from regex import F

master = Tk()

width_value = master.winfo_screenwidth()
height_value = master.winfo_screenheight()


# width_value = 800
# height_value= 400

BigFont=  int(width_value/15)
SmallFont= int(height_value/30)
DiffHeight= int(height_value/8)
LEFTSHIFT = int(width_value/12)

print(width_value,height_value)

master.geometry("%dx%d" % (width_value+0,height_value+ 0))

# master.mainloop()
# import tkinter as tk
# w = tk.Tk()
master.title('main')
# w.geometry('300x300')

mainFirst = Label(master,text="Team1",font=("Helvetica", BigFont))



First = Label(master,text="1st:",font=("Helvetica", SmallFont,"bold"))
Second = Label(master,text="2nd:",font=("Helvetica", SmallFont,"bold"))
Third = Label(master,text="3rd:",font=("Helvetica", SmallFont,"bold"))
Fourth = Label(master,text="4th:",font=("Helvetica", SmallFont,"bold"))
Fifth = Label(master,text="5th:",font=("Helvetica", SmallFont,"bold"))
Sixth = Label(master,text="6th:",font=("Helvetica", SmallFont,"bold"))   

FirstRes= Label(master,text="1",font=("Roboto", SmallFont))
SecondRes= Label(master,text="2",font=("Helvetica", SmallFont))
ThirdRes= Label(master,text="3",font=("Helvetica", SmallFont))
FourthRes= Label(master,text="4",font=("Helvetica", SmallFont))
FifthRes= Label(master,text="5",font=("Helvetica", SmallFont))
SixthRes= Label(master,text="6",font=("Helvetica", SmallFont))

mainFirst.place(x=(width_value/4)-BigFont, y=((height_value/2)-BigFont))
First.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT, y=((height_value/2)-(DiffHeight*3)))
Second.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT, y=((height_value/2)-(DiffHeight*2)))
Third.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT, y=((height_value/2)-DiffHeight))
Fourth.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT, y=((height_value/2)+0))
Fifth.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT, y=((height_value/2)+(DiffHeight)))
Sixth.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT, y=((height_value/2)+(DiffHeight*2)))

FirstRes.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT+150, y=((height_value/2)-(DiffHeight*3)))
SecondRes.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT+150, y=((height_value/2)-(DiffHeight*2)))
ThirdRes.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT+150, y=((height_value/2)-DiffHeight))
FourthRes.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT+150, y=((height_value/2)+0))
FifthRes.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT+150, y=((height_value/2)+(DiffHeight)))
SixthRes.place(x=(width_value/4)+(width_value/2)-LEFTSHIFT+150, y=((height_value/2)+(DiffHeight*2)))

# First.place(x=0, y=0)
# Second.pack()
mainloop()
