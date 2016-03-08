import socket
def Main():
	host='127.0.0.1'
	port= 5001
	server=('127.0.0.1',5000)

	sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	message=input("->")
	while message is not 'q':
		sock.sendto(message.encode('utf-8'),server)
		data, addr=sock.recvfrom(1024)
		print("Recieved from server:"+ data.decode('utf-8'))
		message=input("->")
	sock.close()
if __name__=='__main__':
	Main()