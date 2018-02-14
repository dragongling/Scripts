def generate(event):
	a = unamefield.get()
	x = 0
	for i in a:
		x += (ord(i.lower()) ^ 0x5678 - 0x30) * 0xA ^ 0x1234
	passfield.delete(0,END)
	passfield.insert(END,str(x))


from tkinter import *
root = Tk()
root.resizable(height=False,width=False)

uname = StringVar()
unamefield = Entry(root,width=20,bd=3,textvariable=uname)
username = Label(root,text="Username:")
unamefield.bind('<Return>',generate)

password = Label(root,text="Password:")
pword = StringVar()
passfield = Entry(root,width=20,bd=3,textvariable=pword)

username.pack()
unamefield.pack()
password.pack()
passfield.pack()
root.mainloop()