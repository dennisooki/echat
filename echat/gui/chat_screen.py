import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText


def chat_screen(username, client):
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

    def send_message(message, chat_box):
        message = input_box.get()
        client.send_message(message)  # Use the client's send_message method
        input_box.delete(0, END)

    def exit_chat():
        client.disconnect()
        root.destroy()

    exit_button = Button(root, text="Exit", command=exit_chat)
    exit_button.pack()

    #create a button to send the message
    send_button = Button(root, text="Send", command=lambda: send_message(input_box.get(), chat_box))
    send_button.pack()
    threading.Thread(target=client.receive_messages, args=(chat_box,)).start()
    root.mainloop()
    
