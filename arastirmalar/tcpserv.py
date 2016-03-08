import socket
def Main():
	host='127.0.0.1'
	port=5000

	sock=socket.socket()
	sock.bind((host,port))

	sock.listen(1)
	client, addr = sock.accept()

	print('Connection from:'+ str(addr))
	while 1:
		data = client.recv(1024).decode('utf-8')
		if not data:
			break
		print('From user:'+ data)
		data = data.upper()
		print('Sending...'+ data)
		client.send(data.encode('utf-8'))
	client.close()
if __name__=="__main__":
	Main()