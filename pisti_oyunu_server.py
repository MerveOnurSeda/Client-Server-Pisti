from socket import *
from threading import Thread

def masa(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(4)
    while True:
        client, addr = sock.accept()
        print(str(addr[0]) + "addresi "+str(addr[1]) +" portundan masaya yeni bir oyuncu geldi")
        # Çoklu oyuncu için thread kullanıldı
        #oyunaGir metoduna gelen bağlantı bilgileri parametre olarak gönderildi
        Thread(target = oyunaGir, args = (client,), daemon = True).start()

def oyunaGir(client):
    #Kullanıcıdan veri bekleniyor
    while True:
        req = client.recv(100)
        if not req:
            break
        komut =""
        komut = "4 kart verildi"
        resp =komut.encode('ascii')+b"\n"
        client.send(resp)
        #data = "Oyuncu: "+ str(req)

        ###
        #İşlemler
        ###


        # bağlı oyuncuya gerekli mesaj gönderiliyor

    print("Oyun bitti")
if __name__ is "__main__":
    masa(('',7000))
