#un script 
class Twitter(object):
	""" Define al twitter,
	por @categulario """
	def __init__(yo_mismo, nombre_usuario):
		"""este es el constructor"""
		#son dos guiones bajos
		yo_mismo.usuario = nombre_usuario;
		#el yo_mismo es como el this en java
		#representa el objeto

	def obten_nombre_usuario(yo_mismo):
		"""obtiene el nombre de usuario"""
		return yo_mismo.usuario

if __name__ == "__main__":
	t = Twitter('Categulario') #creo un objeto de la clase
	#esta es la forma de crear un objeto
	print t.obten_nombre_usuario()
