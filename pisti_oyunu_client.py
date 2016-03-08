import socket
def Main():
	host='127.0.0.1'
	port=7000
	sock = socket.socket()
	sock.connect((host,port))
	message=input("->")
	while message is not 'q':
		sock.send(message.encode('utf-8'))
		data = sock.recv(1024).decode('utf-8')
		#print('Recived from server: '+data)
		message=input('->')
	sock.close()
if __name__=="__main__":
	Main()
