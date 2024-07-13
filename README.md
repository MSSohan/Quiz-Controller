# Quiz Controller

Welcome to the Quiz Controller setup guide! Follow the steps below to get everything up and running.

To run the quiz controller, execute the `main.py` script. This script will handle the logic for your quiz event.

### GPIO Pin Setup
First, let's configure the GPIO pins. Below are the pins you'll need to use:


```
Team1 = 11
Team2 = 12
Team3 = 13
Team4 = 15
Team5 = 16
Team6 = 18
reset = 22
buzzer= 24
```
Make sure to set the GPIO pins according to the schematic view of the Raspberry Pi:
<img src="/media/img4.jpg" alt="GPIO Schematic" width="600"/>

### Images from the Event
Here are some snapshots from a recent event where the quiz controller was used. Notice that the team names are positioned according to their pressing time in the corner of the giant screen. The team that pressed the button first has their name displayed in the middle:


<img src="/media/img2.jpg" alt="Team Name Position" width="600"/>

Additionally, there's a low voltage warning displayed on the Raspberry Pi. This is something we'll need to address:


<img src="/media/img3.jpg" alt="Low Voltage Warning" width="600"/>

### Bugs to be Fixed
Here are a few issues we've identified that need fixing:
- [x] Timing issue: This has been resolved.
- [ ] Fix the placement of the team name on the giant screen: The team names should be more prominently displayed.
- [ ] Resolve the low voltage warning: Ensure the Raspberry Pi has a stable power supply.

### Refining whole devices
Finally, here are some images from the manufacturing process of the quiz controller setup. These provide a behind-the-scenes look at the assembly:


<img src="/media/img1.jpg" alt="Manufacturing" width="400"/>

Feel free to reach out if you have any questions or need further assistance with the setup. Happy quizzing!
