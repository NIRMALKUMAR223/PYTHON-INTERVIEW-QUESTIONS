from tkinter import *
from tkinter import font
from tkinter import messagebox

def close():
    w = close
    if messagebox.askyesno("warning","Do you want to quit..?"):
    	exit()
def jet():
    l = Label(window, text = "MAKE SURE YOUR INTERNET IS CONNECTED........!" , fg = "red")
    l.pack()
def get():
    h = you.get()
    messagebox.askyesnocancel("WARNING","Do You Want To Register....?")

window = Tk()
window.title("WEB PAGE")
window.geometry("600x600")

let = Label(window, width = "200" , text = "STUDENT LOGIN" , font = ("times",23) , fg = "black" , bg = "blue" , padx = "15")
let.pack()

let = Label(window, text = "welcome to our collage webside ,enter your student id and password in given bellow", width = "100" , fg = "black")
let.pack()

hit = Button(window ,text = "LOGIN", bg = "green" , fg = "white" , padx = "10" , pady = "10" , activebackground = "white" , activeforeground = "black" , font = ("times",20) , command = jet)
hit.pack(side = "bottom")

gy = Button(window , text = "REGISTER", bg = "orange" , fg = "white" , padx = "10", pady = "10" , activebackground = "white" , command = get)
gy.pack()

hi = Button(window, text = "Forget Password",padx = "20" ,pady = "10" , bg = "green", fg = "white", activebackground = "white", activeforeground = "black")
hi.pack(side = "bottom")

hi = Button(window ,text = "EXIT", bg = "red" , fg = "white" , padx = "10" , pady = "10" , activebackground = "white" , activeforeground = "black", command = close , font = ("times",15))
hi.pack(side = "bottom")

j = Label(text = "ENTER YOUR STUDENT ID" , font = ("bold",10))
j.pack(side = "left")

you = Entry(window)
you.pack(side = "left")

p = Label(text = "ENTER YOUR PASSWORD" , font = ("bold",10))
p.pack(side = "left")

op = Entry(window, fg = "red")
op.pack(side = "left")

m = Label(text = "WELCOME" , font = "times" , width = "10", fg = "black", bg = "yellow")
m.pack()

window.mainloop()
