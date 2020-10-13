import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
window.title("Choose your beverages")
window.geometry("300x200")

def submit_action():
    message_text = ""
    if c_var.get():
        message_text += "You have chosen coffee\n"
    if t_var.get():
        message_text += "You have chosen tea\n"
    if w_var.get():
        message_text += "You have chosen water\n"
    messagebox.showinfo("Test","This is a test message")

submit_button = Button(window, text="submit",
                       command=submit_action)

c_var = BooleanVar()
t_var = BooleanVar()
w_var = BooleanVar()

coffee_cb = Checkbutton (window, text= "Coffee",
                         variable =c_var, onvalue=True,
                         offvalue=False,
                         width=20, height=2)

tea_cb = Checkbutton (window, text="Tea",
                      variable=t_var, onvalue=True,
                      offvalue=False,
                      width=20, height=2)

water_cb= Checkbutton (window, text="Water",
                       variable=w_var, onvalue=True,
                       offvalue=False,
                       width=20, height=2)
water_cb.pack()
tea_cb.pack()
coffee_cb.pack()
submit_button.pack()
window.mainloop()
