import tkinter as tk

import pygame


root=tk.Tk()
root.geometry("500x500")
root.title("snake game")
root.resizable(False,False)
pygame.mixer.init()
#----------------------------Functions---------------------------------
def play():
    fw.forget()
    f1play.pack()

def close():
    root.destroy()


def option():
    fw.forget()
    f2options.pack()

def board():
    fw.forget()
    f3scoreboard.pack()

def back():
    f2options.forget()
    fw.pack()


#----------------------------Main Frames---------------------------------

f1play=tk.Frame(root,width=500,height=500,bg="#e0e0e0")

f2options=tk.Frame(root,width=500,height=500,bg="#191919")

f3scoreboard=tk.Frame(root,width=500,height=500,bg="#191919")

fw=tk.Frame(root,width=500,height=500,bg="black")
fw.pack()
#----------------------------Main Buttons---------------------------------
t1=tk.Button(fw,width=25,height=2,bg="red",fg="white",text="Play",font="arial 16 bold",command=play)
t1.place(x=90,y=55)

t2=tk.Button(fw,width=25,height=2,bg="red",fg="white",text="Options",font="arial 16 bold",command=option)
t2.place(x=90,y=150)

t3=tk.Button(fw,width=25,height=2,bg="red",fg="white",text="Scoreboard",font="arial 16 bold",command=board)
t3.place(x=90,y=250)

t4=tk.Button(fw,width=25,height=2,bg="red",fg="white",text="Quit",font="arial 16 bold",command=close)
t4.place(x=90,y=350)

#----------------------------option frame & buttons---------------------------------

q1=tk.Frame(f2options,width=500,height=500,bg="#e0e0e0")

qw1=tk.Button(f2options,width=25,height=2,bg="red",fg="white",text="Theme 1",font="arial 16 bold")
qw1.place(x=90,y=55)

qw2=tk.Button(f2options,width=25,height=2,bg="red",fg="white",text="Theme 2",font="arial 16 bold")
qw2.place(x=90,y=150)

qw3=tk.Button(f2options,width=25,height=2,bg="red",fg="white",text="Theme 3",font="arial 16 bold")
qw3.place(x=90,y=250)

qw4=tk.Button(f2options,width=8,height=2,bg="red",fg="white",text="Back<=",font="arial 16 bold",command=back)
qw4.place(x=90,y=350)

qw5=tk.Button(f2options,width=8,height=2,bg="red",fg="white",text="Mute",font="arial 16 bold")
qw5.place(x=310,y=350)

























root.mainloop()