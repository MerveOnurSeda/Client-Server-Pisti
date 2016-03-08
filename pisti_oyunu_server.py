from socket import *
from threading import Thread

def masa(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(4)
    while True:
        client, addr = sock.accept()
        print("baglanti", addr)
        # Çoklu oyuncu için thread kullanıldı
        #oyunaGir metoduna gelen bağlantı bilgileri parametre olarak gönderildi
        Thread(target = oyunaGir, args = (client,), daemon = True).start()

def oyunaGir(client):
    #Kullanıcıdan veri bekleniyor
    while True:
        req = client.recv(100)
        if not req:
            break

        data = "Oyuncu: "+ str(req)
        ###
        #İşlemler
        ###

        resp = str(data).encode('ascii')+b"\n"
        # bağlı oyuncuya gerekli mesaj gönderiliyor
        client.send(resp)
    print("Oyun bitti")
if __name__ is "__main__":
    masa(('',7000))
