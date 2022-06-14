import sqlite3
import os


# per creare nuovo account nel database usare :
# database.execute(("INSERT INTO account(username,psw) VALUES (?,?)"),("mouad","lahlal"))

class User:

    def __init__(self, clientsocket):
        self.clientsocket = clientsocket
        self.logged = False    # verifica se l'utente ha effettuato l'accesso
        self.connesso = False  # verifica se l'utente si è connesso alla chat
        self.occupato = False
        self.db = sqlite3.connect(f"{os.getcwd()}\\database.db", check_same_thread=False)

    def verifica_account(self, usr, psw):
        dati = self.db.execute("SELECT username,psw FROM account WHERE username=?", (usr,))
        y = ""

        for x in dati:
            y = str(x)
        y = y.replace("(", "")
        y = y.replace(")", "")
        y = y.replace("'", "")
        y = y.replace(",", "")
        y = y.split()

        if usr == y[0]:
            if psw == y[1]:
                self.logged = True
