from tkinter import *  
import time
from .login_screen import login_screen
from ..db.db_controller import db_first_run
def splash():
    root = Tk()
    root.geometry("400x400")
    root.title("Splash Screen")
    root.config(bg="black")
    Label(root, text="eChat", font=("Arial", 20), fg="white", bg="black").pack(pady=20)
    def close_splash():
        root.destroy()
        login_screen()

    db_first_run()
    root.after(3000, close_splash)
    
    root.mainloop()

splash()