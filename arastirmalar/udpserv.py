import socket

def Main():
	host = '127.0.0.1'
	port= 5000
	sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	sock.bind((host,port))
	print('Server started')
	while 1:
		data, addr= sock.recvfrom(1024)
		print("Message from:"+str(addr).decode('utf-8'))
		print("From user:"+ data.decode('utf-8'))
		data=data.upper()
		print("Sending :"+data)
		sock.sendto(data.encode('utf-8'),addr)
	sock.close()
if __name__=="__main__":
	Main()