import json
import requests
from tkinter import *


class ChatWindow:
    def __init__(self):
        self.window = Tk()
        self.messages = {}

        self.chat_window = Listbox(self.window, width=30, height=20)
        self.name_input = Entry(self.window)
        self.name = 'text'
        self.connect_button = Button(self.window, text='Connect', command=self.connect)
        self.message_input = Entry(self.window)
        self.send_message_button = Button(self.window, text='SEND', command=self.send_message)

        self.name_input.grid(row=0, column=0)
        self.connect_button.grid(row=0, column=1)
        self.chat_window.grid(columnspan=2)
        self.message_input.grid(row=2)
        self.send_message_button.grid(column=1, row=2)

    def connect(self):
        self.name = self.name_input.get()
        response = requests.get('http://dzhenetl.pythonanywhere.com/chat')
        messages = json.loads(response.text)
        for i in messages:
            if i not in self.messages.keys():
                self.messages[i] = messages[i]
        self.show_messages()

    def show_messages(self):
        self.chat_window.delete(0, 'end')
        for i in self.messages:
            message = f'{self.messages[i]["author"]}: {self.messages[i]["text"]}'
            self.chat_window.insert(END, message)

    def send_message(self):
        author = self.name
        text = self.message_input.get()
        message = {"author": f"{author}",
                   "text": f"{text}"}
        requests.post(
            'http://dzhenetl.pythonanywhere.com/chat',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(message)
        )
        self.connect()
        self.message_input.delete(0, 'end')


chat = ChatWindow()
chat.window.title('Messenger')


chat.window.mainloop()
