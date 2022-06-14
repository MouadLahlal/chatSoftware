from socket import *
from threading import Thread
from Crypto import Crypto
from User import User


class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = None
        self.utenti = []
        self.criptatore = Crypto()  # creo oggetto Crypto per criptare/decriptare i messaggi inviati/ricevuti via socket
        self.criptatore.load_key()  # carico la chiave usata per criptare e decriptare i messaggi

    def avvia(self):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.bind((self.host, self.port))
        self.s.listen(5)

    def ascolta(self):
        while True:
            clientsocket, address = self.s.accept()
            t1 = Thread(target=self.client, args=(clientsocket, address,), daemon=True)
            t1.start()

    def client(self, clientsocket, address):
        print(f"Connesso con {address}")
        address = list(address)
        address[1] = int(address[1])
        user = User(clientsocket)
        while not user.logged:
            try:
                usr = self.ricevi(user)
                psw = self.ricevi(user)
                user.verifica_account(usr, psw)
                self.invia(user, str(user.logged))
                print(user.logged)
            except:
                print(f"Connessione terminata da {address}")
                break

        if user.logged:
            self.utenti.append([address[0], address[1], user])
            contatto_host = self.ricevi(user)
            contatto_port = int(self.ricevi(user))
            print(contatto_host, contatto_port)
            user.connesso = True
            self.chat(contatto_host, contatto_port, user)
            #print(f"Connessione terminata da {address}")

    def chat(self, host, port, user):
        destinatario = None
        print(self.utenti)
        for i in self.utenti:
            if host in i[0]:
                if port == i[1]:
                    destinatario = i[2]
                    print("Trovato")
                    break

        thread1 = Thread(target=self.inoltra_msg, args=(user, destinatario,), daemon=True)
        thread2 = Thread(target=self.inoltra_msg, args=(destinatario, user,), daemon=True)

        while True:
            if destinatario.connesso:
                thread1.start()
                print("avviato thread 1")
                thread2.start()
                print("avviato thread 2")
                break

    def inoltra_msg(self, mittente, destinatario):
        while True:
            msg = self.ricevi(mittente)
            self.invia(destinatario, msg)

    def invia(self, user, msg):
        msg = self.criptatore.encrypt_info(msg)
        user.clientsocket.send(msg)

    def ricevi(self, user):
        msg = user.clientsocket.recv(1024)
        msg = self.criptatore.decrypt_info(msg)
        return msg
