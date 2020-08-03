#from socket import AF_INET, socket, SOCK_STREAM
#from threading import Thread
from tkinter import *


def r_mail(r_from,r_title,r_body):
	global top
	top = Tk()
	top.title("Received Mail")
	top.configure(bg="white")

	main = Frame(top, height=200, width=200,bg="white")
	main.pack(side = TOP)
	
	lbl_to = Label(main,font=('arial',16,'bold'), text="From\t:", bd=10, anchor="w", bg="white",fg="red",width=8)
	lbl_to.grid(row=0,column=0)
	lbl_title = Label(main,font=('arial',16,'bold'), text="Title\t:", bd=10, anchor="w", bg="white",fg="red",width=8)
	lbl_title.grid(row=1,column=0)
	lbl_body = Label(main,font=('arial',16,'bold'), text="Body\t:", bd=10, anchor="w", bg="white",fg="red",width=8)
	lbl_body.grid(row=2,column=0)
	
	global txt_to,txt_title,txt_body

	txt_to = Text(main,font=('arial',16,'bold'), bd=0, insertwidth=1, bg="white",height=2,width=40)
	txt_to.grid(row=0,column=1)
	txt_to.insert(INSERT,r_from)
	txt_to.configure(state = 'disabled')
	txt_title = Text(main,font=('arial',16,'bold'), bd=0, insertwidth=1, bg="white",height=2,width=40)
	txt_title.grid(row=1,column=1)
	txt_title.insert(INSERT,r_title)
	txt_title.configure(state = 'disabled')
	txt_body = Text(main,font=('arial',16,'bold'), bd=0, insertwidth=1, bg="white",height=10,width=40)
	txt_body.grid(row=2,column=1)
	txt_body.insert(INSERT,r_body)
	txt_body.configure(state = 'disabled')


	top.mainloop()
	#return [to,title,body]
	
