from Login import Login
from Client import Client
from threading import Thread


client = Client("192.168.1.87", 9999)
client.avvia()

frm_login = Login(client)
frm_login.avvia()
