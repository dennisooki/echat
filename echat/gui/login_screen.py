#implement a simple login screen with  username and password fields centered in a callable function named login_screen(), the input should be passed to a function called login_handler() with a TODO attestaion, also add a register button that navigates to register_screen()

from tkinter import *
from tkinter import messagebox
from ..chatclient.client_auth import user_login, user_register
from .chat_screen import chat_screen

def login_screen():
    root = Tk()
    root.title("Login Screen")
    root.geometry("400x300")

    username_label = Label(root, text="Username:")
    username_label.pack()

    username_entry = Entry(root)
    username_entry.pack()

    password_label = Label(root, text="Password:")
    password_label.pack()

    password_entry = Entry(root, show="*")
    password_entry.pack()

    def login_event():
        username = username_entry.get()
        password = password_entry.get()
        loginBool, info = user_login(username, password)
        messagebox.showinfo(title="Login Status", message=info)
        #if loginBool is true navigate to chat screen and destroy login screen
        if loginBool:
            root.destroy()
            chat_screen(username)
        

    login_button = Button(root, text="Login", command=login_event)
    login_button.pack()

    register_button = Button(root, text="Register", command=register_screen)
    register_button.pack()


    root.mainloop()

def register_screen():
    root = Tk()
    root.title("Register Screen")
    root.geometry("400x300")

    username_label = Label(root, text="Username:")
    username_label.pack()

    username_entry = Entry(root)
    username_entry.pack()

    password_label = Label(root, text="Password:")
    password_label.pack()

    password_entry = Entry(root, show="*")
    password_entry.pack()

    def register_event():
        username = username_entry.get()
        password = password_entry.get()
        registerBool, info = user_register(username, password)
        messagebox.showinfo(title="Register Status", message=info)
        #if registerBool is true navigate to login screen and destroy register screen
        if registerBool:
            root.destroy()
            

    register_button = Button(root, text="Register", command=register_event)
    register_button.pack()


    root.mainloop()

 
