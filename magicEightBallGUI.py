import random
import time
from tkinter import *

#List of potential answers the Magic 8 Ball will give
answersList = ["Definitely!", "Forget about it", "I'm not sure", "Yes!", "No!", "Ask again later.", "It is certain.", "Most likely.", "Probably not.", "Doubtful.", "You can rely on it.", "Without a doubt!", "My sources say no."]

window = Tk()

#Title
window.title("Magic 8 Ball Application")

#Header
lbl = Label(window, text="Welcome to Magic 8 Ball!", font=("Verdana", 30))
lbl.place(x=300, y=75, anchor="center")

#User Question Entry Field
userinput = Entry(window, width=50)
userinput.place(x=300, y=165, anchor="center")

#Defining what happens when the Button is pushed
def callback():
    thinkinglbl = Label(window, text="Mmmmh....")
    thinkinglbl.place(x=300, y=250, anchor="center")
    time.sleep(1)
    answerlbl = Label(window, text=random.choice(answersList), font=("Verdana", 24))
    answerlbl.place(x=300, y=300, anchor="center")

#Button
btn = Button(window, text="Ask A Question", command=callback, font=("Verdana", 14), fg="navy", padx=5, pady=5)
btn.place(x=300, y=200, anchor="center")

#Window Size
window.geometry('600x400')

window.mainloop()

