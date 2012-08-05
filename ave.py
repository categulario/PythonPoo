#experimentos con clases

class Ave(object):
	"""define un ave"""
	def __init__(self, tamanio):
		"""inicializa el ave"""
		self.tamanio = tamanio

	@staticmethod
	def volar(distancia):
		"""vuela un tramo"""
		#funcion estatica
		for i in xrange(distancia):
			print "estoy volando", i

class Colibri(Ave):
	def __init__(self, color):
		"""inicializa un Colibri"""
		#super.__init__(self, 'chico')
		self.color = color
		self.panza = 0
		#super(Ave, self).__init__('chico')

	def comer(self, comida):
		#no es estatica
		if comida:
			self.panza += 10

if __name__ == "__main__":
	#metodo estatico
	Colibri.volar(10)
	#metodo no estatico
	c = Colibri('verde')
	c.comer(2)