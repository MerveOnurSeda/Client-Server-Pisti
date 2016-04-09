import socket
from pisti import Kart
import json
def Main():
	host='127.0.0.1'
	port=2000
	sock = socket.socket()
	sock.connect((host,port))

	self.oyuncu1 = Oyuncu(1)
	self.oyuncu2 = Oyuncu(2)
	message=json.dumps(Kart("Maca","As").__dict__)
	sock.send(message.encode('utf-8'))
	sock.close()
if __name__=="__main__":
	Main()
