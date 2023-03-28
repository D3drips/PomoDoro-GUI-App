from tkinter import *
import math
reps=0
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
timer2=NONE
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
def reset():
    window.after_cancel(timer2)
    canvas.itemconfig(timer,text="00:00")
    global reps
    reps=0
def start():
    global reps
    reps += 1
    work=WORK_MIN*60
    break1=SHORT_BREAK_MIN*60
    longbreak=LONG_BREAK_MIN*60
    if reps%8==0:
         countdown(longbreak)
         mylabel.config(text="Long break",bg=YELLOW,fg=RED,font=(FONT_NAME,45,"bold"))
    elif reps%2==0:
        mylabel.config(text="Short break",bg=YELLOW,fg=RED,font=(FONT_NAME,45,"bold"))
        countdown(break1)
    else:
        mylabel.config(text="Work",bg=YELLOW,fg=RED,font=(FONT_NAME,45,"bold"))
        countdown(work)
window=Tk()
window.config(padx=100,pady=50,bg=GREEN)
window.title("PomoDoro Widget")
mylabel=Label(text="Timer",bg=YELLOW,fg=RED,font=(FONT_NAME,45,"bold"))
mylabel.grid(column=1,row=0)
canvas= Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
ing=PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=ing)
def nidd():
    countdown(5*60)
but1=Button(text="start", height=1, command=start)
def countdown(count):
    minute=math.floor(count/60)
    second=count%60
    if second<10:
        temp=second
        second=f"0{temp}"
    if second==0:
        second="00"
    if count>0:
        global timer2
        canvas.itemconfig(timer,text=f"{minute}:{second}")
        timer2=window.after(1000,countdown,count-1)
    else:
        start()
but1.grid(column=0,row=3)
but2=Button(text="reset",height=1,command=reset)
but2.grid(column=3,row=3)
timer=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)















window.mainloop()