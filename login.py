from tkinter import*

def log():
	root=Tk()
	root.winfo_x()
	root.winfo_y()
	root.configure(bg="white")
	root.title("Intranet Mailing System")

	Tops = Frame(root, width= 1000, height=50 , bg="white" )
	Tops.pack(side=TOP)

	f1 = Frame(root, width=1000, height=5 , relief=SUNKEN, bg="red")
	f1.pack(side=TOP)

	f3 = Frame(root, width=1000, height=150 , relief=SUNKEN, bg="white")
	f3.pack(side=TOP)

	f2 = Frame(root, width=1000, height=500 , relief=SUNKEN, bg="white")
	f2.pack(side=TOP)

	f6 = Frame(root, width=1000, height=10 , relief=SUNKEN, bg="white")
	f6.pack(side=TOP)

	f5 = Frame(root, width=1000 , relief=SUNKEN, bg="white")
	f5.pack(side=TOP)

	f4 = Frame(root, width=1000, height=150 , relief=SUNKEN, bg="white")
	f4.pack(side=TOP)

	lblInfo = Label(Tops, font=('arial',50,'bold'), text = "INTRANET MAIL", fg = "red", bd=10, anchor='w',bg="white")
	lblInfo.pack()

	username = StringVar()
	password = StringVar()

	lbl_username = Label(f2,font=('arial',16,'bold'), text="username", bd=10, anchor="w", bg="white",fg="red")
	lbl_username.grid(row=0,column=0)
	txt_username = Entry(f2,font=('arial',16,'bold'), textvariable=username, bd=0, insertwidth=4, bg="pink", fg="red",justify="right")
	txt_username.grid(row=0,column=2)

	lbl_password = Label(f2,font=('arial',16,'bold'), text="password", bd=10, anchor="w", bg="white",fg="red")
	lbl_password.grid(row=1,column=0)
	txt_password = Entry(f2,font=('arial',16,'bold'), show="*",textvariable=password, bd=0, insertwidth=4, bg="pink", fg="red", justify="right")
	txt_password.grid(row=1,column=2)

	btn_login=Button(f5, fg="white", font=('arial',16,'bold'),width=10, bd=10,text="login", bg="red", command = root.destroy).grid()


	root.mainloop()
	
	return [username,password]
