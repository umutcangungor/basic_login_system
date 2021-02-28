from tkinter import *
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
import tkinter as tk






class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+250+150")
        self.root.tk.call("wm","iconphoto",self.root._w,tk.PhotoImage(file="images/Icon-Small.ico"))


        ##IMAGES
        self.login_icon=ImageTk.PhotoImage(file="images/4827229.jpg")
        self.password_icon = ImageTk.PhotoImage(file="images/Icon-Small-50.png")
        self.user_icon = ImageTk.PhotoImage(file="images/Icon-Small-50@2x.png")
        self.user_icon_mini = ImageTk.PhotoImage(file="images/Icon-Small-40.png")

        #IMAGES END

        #Variables
        self.uname=StringVar()
        self.pass_=StringVar()


        #

        bg_label = Label(self.root, image=self.login_icon).pack()
        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="snow",fg="steelblue",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        login_frame=Frame(self.root,bg="white smoke")
        login_frame.place(x=300,y=150)

        logo_label=Label(login_frame,image=self.user_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        user_label=Label(login_frame,text="Username",image=self.user_icon_mini,compound=LEFT,font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=10)
        user_text=Entry(login_frame,textvariable=self.uname,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20,pady=20)


        password_label=Label(login_frame,text="Password",image=self.password_icon,compound=LEFT,font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=10)
        password_text = Entry(login_frame, bd=5,textvariable=self.pass_, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20)

        btn_log=Button(login_frame,text="Login",command=self.login,width=15,font=("times new roman",15,"bold"),bg="steelblue",fg="white smoke").grid(row=3,column=1,padx=0,pady=20)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are required !")
        elif self.uname.get()=="umutcan" and self.pass_.get()=="123":
            messagebox.showerror("Succesful","Welcome Umutcan Güngör !")
        else:
            messagebox.showerror("Error","Username or Password is Wrong !")



root=Tk()
obj=login_system(root)
root.mainloop()
