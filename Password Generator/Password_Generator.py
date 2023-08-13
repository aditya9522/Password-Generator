from tkinter import *
import random

root = Tk()
root.geometry("600x300")
root.title("Password Generator")
root.configure(background="pink",border=10)
l = StringVar()
passwd = StringVar()
l.set("")

def show():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "@#$%^&*~|/\?./"
    numbers = "0123456789"
    ans = lower_case + upper_case + symbols + numbers
    length = l.get()
    password = "".join(random.sample(ans, int(length)))

    passwd.set(str(password))



top = Label(root,text="Password Generator",font=("arial",16,"bold"),bg="pink",fg="red",width=20).pack()
l1 = Label(root,text="Enter Length of Password",font=("arial",12,"bold"),bg="pink",fg="blue").place(x=170,y=100)
e1 = Entry(root,font=("arial",12,"bold"),bg="yellow",fg="green",width=25,textvariable=l).place(x=170,y=130)
l2 = Button(root,text="show password",font=("arial",12,"bold"),bg="white",fg="black",command=show).place(x=170,y=160)
e1 = Entry(root,textvariable=passwd,bd=0,font=("arial",15,"bold"),bg="pink",fg="black").place(x=200,y=220)


root.mainloop()