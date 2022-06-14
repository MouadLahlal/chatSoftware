import tkinter as tk
from tkinter import Scrollbar
from threading import Thread


class Chat:

    def __init__(self, client):
        self.client = client
        self.root = tk.Tk()
        self.root.title("Chat")
        self.root.geometry("300x200")
        self.txt_msg = tk.Text(self.root, height=1, width=30)
        self.btn_invia = tk.Button(self.root, text="INVIA", command=self.invia)
        self.scroll = tk.Scrollbar(self.root)
        self.messaggi = tk.Listbox(self.root, yscrollcommand=self.scroll.set)

    def avvia(self):
        self.chat()
        self.txt_msg.pack()
        self.btn_invia.pack()
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.messaggi.pack(fill=tk.BOTH)
        self.scroll.config(command=self.messaggi.yview)
        self.root.mainloop()

    def invia(self):
        msg = self.txt_msg.get("1.0", "end-1c")
        self.client.invia(msg)

    def chat(self):
        def ricevi_messaggi():
            while True:
                msg = self.client.ricevi()
                self.messaggi.insert(tk.END, msg)
                """label = tk.Label(self.scroll, text=msg)
                label.pack()"""

        t1 = Thread(target=ricevi_messaggi, daemon=True)
        t1.start()
