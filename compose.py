#from socket import AF_INET, socket, SOCK_STREAM
#from threading import Thread
from tkinter import *

def send():
	global to,title,body	
	to = txt_to.get("1.0","end-1c")
	title = txt_title.get("1.0","end-1c")
	body = txt_body.get("1.0","end-1c")
	top.destroy()


def mail():
	global top
	top = Tk()
	top.title("compose")
	top.configure(bg="white")

	main = Frame(top, height=200, width=200,bg="white")
	main.pack(side = TOP)
	f1 = Frame(top,height = 30,width=200)
	f1.pack(side = TOP)

	lbl_to = Label(main,font=('arial',16,'bold'), text="to\t:", bd=10, anchor="w", bg="white",fg="red",width=8)
	lbl_to.grid(row=0,column=0)
	lbl_title = Label(main,font=('arial',16,'bold'), text="title\t:", bd=10, anchor="w", bg="white",fg="red",width=8)
	lbl_title.grid(row=1,column=0)
	lbl_body = Label(main,font=('arial',16,'bold'), text="body\t:", bd=10, anchor="w", bg="white",fg="red",width=8)
	lbl_body.grid(row=2,column=0)
	
	global txt_to,txt_title,txt_body

	txt_to = Text(main,font=('arial',16,'bold'), bd=0, insertwidth=1, bg="white",height=2,width=40)
	txt_to.grid(row=0,column=1)
	txt_title = Text(main,font=('arial',16,'bold'), bd=0, insertwidth=1, bg="white",height=2,width=40)
	txt_title.grid(row=1,column=1)
	txt_body = Text(main,font=('arial',16,'bold'), bd=0, insertwidth=1, bg="white",height=10,width=40)
	txt_body.grid(row=2,column=1)

	btn_send=Button(f1, fg="white", font=('arial',16,'bold'),width=10,bd=10,text="send", bg="red",command = lambda:send()).grid()

	top.mainloop()
	return [to,title,body]
	
