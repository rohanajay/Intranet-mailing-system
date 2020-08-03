#from socket import AF_INET, socket, SOCK_STREAM
#from threading import Thread
from tkinter import *

def read():
	global output
	output = "read"
	top.destroy()
	
def write():
	global output
	output = "write"
	top.destroy()

def op():
	global top
	top = Tk()
	top.title("Operation")
	top.configure(bg="white")

	main = Frame(top, height=200, width=200,bg="white")
	main.pack(side = TOP)
	
	btn_read = Button(main, fg="white", font=('arial',16,'bold'), width=10, bd=10, text="read", bg="red",command= lambda:read()).grid(row=0,column=0)
	btn_write = Button(main, fg="white", font=('arial',16,'bold'), width=10, bd=10, text="write", bg="red",command= lambda:write()).grid(row=0,column=1)

	top.mainloop()
	return output
	
