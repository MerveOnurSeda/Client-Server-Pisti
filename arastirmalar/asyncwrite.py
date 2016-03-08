import threading
import time
class AsyncWrite(threading.Thread):
	def __init__(self, text, out):
		threading.Thread.__init__(self)
		self.text=text
		self.out=out
	def run(self):
		f=open(self.out, 'a')
		f.write(self.text+"\n")
		f.close()
		time.sleep(1)
		print("Finished Writing to "+ self.out)
def Main():
	message=input("Enter string:")
	background=AsyncWrite(message,'out.txt')
	background.start()
	print("Some calculations")
	background.join()
	print("Waited for thread")
if __name__=="__main__":
	Main()