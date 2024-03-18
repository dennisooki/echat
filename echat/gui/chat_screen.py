#create a basic chat screen in tkinter with an input box and a send button
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def chat_screen(username):
    root = Tk()
    root.title(f"eChat: {username}")
    root.geometry("400x500")

    #create a label for the username
    username_label = Label(root, text=f"Welcome, {username}")
    username_label.pack()

    #create a text box for the chat
    chat_box = ScrolledText(root, height=20, width=50)
    chat_box.pack()
    chat_box['state'] = 'disabled'


    #create a text box for the input
    input_box = Entry(root, width=50)
    input_box.pack()

    def send_message(message, username, chat_box):
        chat_box['state'] = 'normal'  # Enable the text box
        chat_box.insert(END, f"{username}: {message}\n")
        chat_box['state'] = 'disabled'  # Disable the text box again
        input_box.delete(0, END)

    #create a button to send the message
    send_button = Button(root, text="Send", command=lambda: send_message(input_box.get(),username, chat_box))
    send_button.pack()

    root.mainloop()
    
