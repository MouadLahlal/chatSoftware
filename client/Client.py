from socket import *
from Crypto import Crypto


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = None
        self.criptatore = Crypto()
        self.criptatore.load_key()

    def avvia(self):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((self.host, self.port))

    def invia(self, msg):
        msg = self.criptatore.encrypt_info(msg)
        self.s.send(msg)

    def ricevi(self):
        msg = self.s.recv(1024)
        msg = self.criptatore.decrypt_info(msg)
        return msg
