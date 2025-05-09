# Import Required Libraries
from tkinter import *
import datetime
import time
from threading import Thread
import pygame

pygame.init()
pygame.mixer.init()

root = Tk()
root.geometry("400x200")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake up")
            pygame.mixer.music.load("sound.mp3")  
            pygame.mixer.music.play()
            break

Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = [f"{i:02d}" for i in range(24)]
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)

minute = StringVar(root)
minutes = [f"{i:02d}" for i in range(60)]
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

second = StringVar(root)
seconds = [f"{i:02d}" for i in range(60)]
second.set(seconds[0])
OptionMenu(frame, second, *seconds).pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

root.mainloop()
