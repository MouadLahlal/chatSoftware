import tkinter as tk
from tkinter import messagebox
from Home import Home


class Login:

    def __init__(self, client):
        self.client = client
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x200")
        self.lbl_username = tk.Label(self.root, text="Username")
        self.lbl_psw = tk.Label(self.root, text="Password")
        self.txt_username = tk.Text(self.root, height=1, width=30)
        self.txt_psw = tk.Text(self.root, height=1, width=30)
        self.btn_invia = tk.Button(self.root, text="INVIA", command=self.invia)

    def avvia(self):
        self.lbl_username.pack()
        self.txt_username.pack()
        self.lbl_psw.pack()
        self.txt_psw.pack()
        self.btn_invia.pack()
        self.root.mainloop()

    def invia(self):
        usr = self.txt_username.get('1.0', 'end-1c')
        psw = self.txt_psw.get('1.0', 'end-1c')
        self.client.invia(usr)
        self.client.invia(psw)
        logged = self.client.ricevi()
        if logged == "True":
            self.root.destroy()
            home = Home(self.client)
            home.avvia()
        else:
            messagebox.showerror("Errore", "Credenziali errate, riprova")
