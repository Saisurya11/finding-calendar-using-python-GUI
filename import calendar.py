import calendar
from tkinter import *

win = Tk()
win.config(background="yellow")
win.title("calendar")
win.geometry("900x700")

la = Label(win, text="enter the year", font=('arial', 23, 'bold'))
la.place(x=270, y=12)
en_text = StringVar()
en = Entry(win, textvariable=en_text, font=('Italic', 23, 'bold')).place(x=500, y=12)

def yearfinder():
    en1 = int(en_text.get())
    year = calendar.calendar(en1)
    # Modify the existing label (la1) instead of creating a new one
    la1.config(text=year)

sub = Button(win, text='Submit', activebackground='grey', background='#C6D5BA', font=('Lato', 15, 'bold'), command=yearfinder).place(x=460, y=90)
la1 = Label(win, width=80, height=35)
la1.place(x=30, y=140)
Label(win,text="*note dates are somewhat shifted to right side").place(x=600,y=200)
win.mainloop()
