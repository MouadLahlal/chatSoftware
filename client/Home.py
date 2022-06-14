import tkinter as tk
from Chat import Chat


class Home:

    def __init__(self, client):
        self.client = client
        self.root = tk.Tk()
        self.root.title("Home")
        self.root.geometry("300x200")
        self.lbl_ip = tk.Label(self.root, text="Inserisci ip")
        self.lbl_port = tk.Label(self.root, text="Inserisci porta a cui connettersi")
        self.txt_ip = tk.Text(self.root, height=1, width=30)
        self.txt_port = tk.Text(self.root, height=1, width=30)
        self.btn_connect = tk.Button(self.root, text="Connetti", command=self.connetti)
        print(self.client.s)

    def avvia(self):
        self.lbl_ip.pack()
        self.txt_ip.pack()
        self.lbl_port.pack()
        self.txt_port.pack()
        self.btn_connect.pack()
        self.root.mainloop()

    def connetti(self):
        host = self.txt_ip.get("1.0", "end-1c")
        port = self.txt_port.get("1.0", "end-1c")
        self.client.invia(host)
        self.client.invia(port)
        self.root.destroy()
        chat = Chat(self.client)
        print("Chat avviata")
        chat.avvia()


"""
self.client2 = Client(host, port)
self.client2.avvia()
chat = Chat()
chat.avvia()
self.root.destroy()
"""
