from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

team1 = 11
team2 = 12
team3 = 13
team4 = 15
team5 = 16
team6 = 18

GPIO.setup(team1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(team2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(team3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(team4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(team5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(team6, GPIO.IN, pull_up_down=GPIO.PUD_UP)


li = []

while(1):
    if GPIO.input(team1) == 0:
        if "team1" not in li:
            print("Team 1 was pressed")
            li.append("team1")
            print(li)
    if GPIO.input(team2) == 0:
        if "team2" not in li:
            print("Team 2 was pressed")
            li.append("team2")
            print(li)
    if GPIO.input(team3) == 0:
        if "team3" not in li:
            print("Team 3 was pressed")
            li.append("team3")
            print(li)
    if GPIO.input(team4) == 0:
        if "team4" not in li:
            print("Team 4 was pressed")
            li.append("team4")
            print(li)
    if GPIO.input(team5) == 0:
        if "team5" not in li:
            print("Team 5 was pressed")
            li.append("team5")
            print(li)
    if GPIO.input(team6) == 0:
        if "team6" not in li:
            print("Team 6 was pressed")
            li.append("team6")
            print(li)
