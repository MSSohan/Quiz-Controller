import time
from tkinter import *
import RPi.GPIO as GPIO

# Set up GPIO mode
GPIO.setmode(GPIO.BOARD)

# Initialize Tkinter master window
master = Tk()

# Get screen dimensions
width_value = master.winfo_screenwidth()
height_value = master.winfo_screenheight()

# Define font sizes and layout parameters based on screen dimensions
BigFont = int(width_value / 15)
SmallFont = int(height_value / 30)
DiffHeight = int(height_value / 8)
LeftGap = int(width_value / 12)
BackgroundColor = "black"
FontColor = "white"

# Print screen dimensions (for debugging)
print(width_value, height_value)

# Configure master window
master.geometry("%dx%d" % (width_value, height_value))
master.configure(bg=BackgroundColor)
master.wm_attributes("-fullscreen", "True")
master.title('main')

# Define GPIO pins for teams and buzzer
Team1, Team2, Team3, Team4, Team5, Team6 = 11, 12, 13, 15, 16, 18
reset, buzzer = 22, 24

# Set up GPIO pins
GPIO.setup(Team1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Team6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(buzzer, GPIO.LOW)

# Function to handle buzzer timing
def timeFunc():
    millis = lambda: int(time.time() * 1000)
    return millis()

# Main function to test team button presses
def test():
    li = []
    millis = lambda: int(time.time())
    Buzzer = False
    try:
        while True:
            if GPIO.input(Team1) == 0 and "Team1" not in li:
                print("Team 1 was pressed")
                li.append("Team1")
                print(li)
            if GPIO.input(Team2) == 0 and "Team2" not in li:
                print("Team 2 was pressed")
                li.append("Team2")
                print(li)
            if GPIO.input(Team3) == 0 and "Team3" not in li:
                print("Team 3 was pressed")
                li.append("Team3")
                print(li)
            if GPIO.input(Team4) == 0 and "Team4" not in li:
                print("Team 4 was pressed")
                li.append("Team4")
                print(li)
            if GPIO.input(Team5) == 0 and "Team5" not in li:
                print("Team 5 was pressed")
                li.append("Team5")
                print(li)
            if GPIO.input(Team6) == 0 and "Team6" not in li:
                print("Team 6 was pressed")
                li.append("Team6")
                print(li)
            if GPIO.input(reset) == 0:
                li.clear()
                Sound = True
                Buzzer = False
                print(li)
            try:
                # Update display labels based on team presses
                if li:
                    FirstRes['text'] = li[0]
                    mainFirst['text'] = li[0]
                else:
                    FirstRes['text'] = " "
                    mainFirst['text'] = " READY!! "
                
                SecondRes['text'] = li[1] if len(li) > 1 else " "
                ThirdRes['text'] = li[2] if len(li) > 2 else " "
                FourthRes['text'] = li[3] if len(li) > 3 else " "
                FifthRes['text'] = li[4] if len(li) > 4 else " "
                SixthRes['text'] = li[5] if len(li) > 5 else " "
                
                # Handle buzzer
                if len(li) == 1 and not Buzzer:
                    GPIO.output(buzzer, GPIO.HIGH)
                    trigger = millis()
                    Buzzer = True
                
                if Buzzer and (millis() - trigger) >= 1:
                    GPIO.output(buzzer, GPIO.LOW)
            except Exception as e:
                print("Display update error:", e)
            
            master.update()
    except KeyboardInterrupt:
        print("Program interrupted")

# Create labels for displaying team results
mainFirst = Label(master, font=("Roboto", BigFont), bg=BackgroundColor, fg=FontColor)

First = Label(master, text="1st:", font=("Helvetica", SmallFont, "bold"), bg=BackgroundColor, fg=FontColor)
Second = Label(master, text="2nd:", font=("Helvetica", SmallFont, "bold"), bg=BackgroundColor, fg=FontColor)
Third = Label(master, text="3rd:", font=("Helvetica", SmallFont, "bold"), bg=BackgroundColor, fg=FontColor)
Fourth = Label(master, text="4th:", font=("Helvetica", SmallFont, "bold"), bg=BackgroundColor, fg=FontColor)
Fifth = Label(master, text="5th:", font=("Helvetica", SmallFont, "bold"), bg=BackgroundColor, fg=FontColor)
Sixth = Label(master, text="6th:", font=("Helvetica", SmallFont, "bold"), bg=BackgroundColor, fg=FontColor)

FirstRes = Label(master, font=("Helvetica", SmallFont), bg=BackgroundColor, fg=FontColor)
SecondRes = Label(master, font=("Helvetica", SmallFont), bg=BackgroundColor, fg=FontColor)
ThirdRes = Label(master, font=("Helvetica", SmallFont), bg=BackgroundColor, fg=FontColor)
FourthRes = Label(master, font=("Helvetica", SmallFont), bg=BackgroundColor, fg=FontColor)
FifthRes = Label(master, font=("Helvetica", SmallFont), bg=BackgroundColor, fg=FontColor)
SixthRes = Label(master, font=("Helvetica", SmallFont), bg=BackgroundColor, fg=FontColor)

# Place labels on the screen
mainFirst.place(x=(width_value / 4) - (BigFont * 2), y=(height_value / 2) - BigFont)
First.place(x=(width_value / 4) + (width_value / 2) - LeftGap, y=(height_value / 2) - (DiffHeight * 2))
Second.place(x=(width_value / 4) + (width_value / 2) - LeftGap, y=(height_value / 2) - DiffHeight)
Third.place(x=(width_value / 4) + (width_value / 2) - LeftGap, y=(height_value / 2))
Fourth.place(x=(width_value / 4) + (width_value / 2) - LeftGap, y=(height_value / 2) + DiffHeight)
Fifth.place(x=(width_value / 4) + (width_value / 2) - LeftGap, y=(height_value / 2) + (DiffHeight * 2))
Sixth.place(x=(width_value / 4) + (width_value / 2) - LeftGap, y=(height_value / 2) + (DiffHeight * 3))

FirstRes.place(x=(width_value / 4) + (width_value / 2) - LeftGap + 150, y=(height_value / 2) - (DiffHeight * 2))
SecondRes.place(x=(width_value / 4) + (width_value / 2) - LeftGap + 150, y=(height_value / 2) - DiffHeight)
ThirdRes.place(x=(width_value / 4) + (width_value / 2) - LeftGap + 150, y=(height_value / 2))
FourthRes.place(x=(width_value / 4) + (width_value / 2) - LeftGap + 150, y=(height_value / 2) + DiffHeight)
FifthRes.place(x=(width_value / 4) + (width_value / 2) - LeftGap + 150, y=(height_value / 2) + (DiffHeight * 2))
SixthRes.place(x=(width_value / 4) + (width_value / 2) - LeftGap + 150, y=(height_value / 2) + (DiffHeight * 3))

# Run the test function
test()

# Start the Tkinter main loop
master.mainloop()
