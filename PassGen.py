import random
import string
import tkinter.messagebox
from tkinter import *




Windows = Tk()
Windows.title("Password Generated")
Windows.config(width=600,height=400,pady=10,padx=10)

def generatePass():
        ran = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        passInput.insert(0,string=ran)



def savefile():
    wname = websiteName.get()
    uname = UserInput.get()
    pword = passInput.get()

    if wname and uname and pword:
        with open("pass.txt", 'a') as passfile:
            passfile.write(f"{wname} | {uname} | {pword} \n")
            passInput.delete(0,END)
            websiteName.delete(0,END)

            tkinter.messagebox.showinfo(title="Password Generator", message="Password successfully saved!")
    else:
        tkinter.messagebox.showerror(title="Password generator",message="Fields missing")








imageFile = PhotoImage(file="logo.png")
imageContainer = Canvas(width=500,height=200,bg="green")
imageContainer.create_image(250,100,image=imageFile)
imageContainer.grid(column=0,row=0,columnspan=3)

website = Label(text="Website",width=20)
website.grid(column=0,row=1)

websiteName = Entry(width=30)
websiteName.grid(column=1,row=1,columnspan=2)



username = Label(text="Username",width=20)
username.grid(column=0,row=2)

UserInput = Entry(width=30)
UserInput.grid(column=1,row=2,columnspan=2)



password = Label(text="Password" ,width=20)
password.grid(column=0,row=3)

passInput = Entry(width=12)
passInput.grid(column=1,row=3)
generate = Button(text="Generate",width=12,command=generatePass)
generate.grid(column=2,row=3)

add = Button(text="Add",width=30,command=savefile)
add.grid(column=1,row=4,columnspan=2)









Windows.mainloop()
