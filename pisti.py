import random

class Kart(object):
	def __init__(self,tip, numara):
		self.tip=tip
		self.numara = numara

	def __str__(self):
		return self.tip+" "+self.numara

class Oyuncu(object):
	def __init__(self, oid):
		self.oid = oid
		self.el = []
		self.kazanc = []
		self.pisti=0

class Pisti(object):
	def __init__(self):
		self.oyuncu1 = Oyuncu(1)
		self.oyuncu2 = Oyuncu(2)
		self.deste = self.deste_olustur()
		self.masa = []
		self.basla()

	def basla(self):
		print("Oyun basladi")
		self.masa = self.deste[:4]
		self.oyuncu1.el = self.deste[4:8]
		self.oyuncu2.el = self.deste[8:12]
		self.deste = self.deste[12:]

	def kart_ver(self):
		# Debug
		try:
			print("Kart verildi")
			self.oyuncu1.el.extend(self.deste[:4])
			self.oyuncu2.el.extend(self.deste[4:8])
			self.deste=self.deste[8:]
		except IndexError:
			print("Oyun bitti")


	def deste_olustur(self):
		kart_tipi = ["kupa","karo","sinek","maca"]
		kart_numarasi = ["As","2","3","4","5","6","7","8","9","10","Vale","Kız","Papaz"]
		kartlar = []
		for t in kart_tipi:
			for n in kart_numarasi:
				kartlar.append(Kart(t,n))
		random.shuffle(kartlar)
		return kartlar


	#Arayüzde
	def kart_kontrol(self,oyuncu):

		if len(self.oyuncu.el)==0:
			self.kart_ver()

	def kart_at(self, oyuncu, kart):
		try:
			print("Kart atildi")
			self.masa.append(kart)
			oyuncu.el.remove(kart)
			if len(self.masa) is 2 and self.masa[-1].numara is self.masa[-2].numara:
				oyuncu.pisti+=10
				print(str(oyuncu.oid)+" pisti yapti")
				self.masa.clear()
			else:
				try:
					
					if kart.numara is "Vale" or self.masa[-2].numara is kart.numara:
						print(str(oyuncu.oid)+" skor yapti")
						oyuncu.kazanc.extend(self.masa)
						self.masa.clear()

				except IndexError:
					pass
		except IndexError as e1:
			print("Hata")
			self.kart_ver()


if __name__ =="__main__":
	p = Pisti()
	try:
		for i in range(52):
				p.kart_at(p.oyuncu1, p.oyuncu1.el[0])
				p.kart_at(p.oyuncu2, p.oyuncu2.el[0])
	except IndexError as e:
		p.kart_ver()
		