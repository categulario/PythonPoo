# -*- coding: utf-8 -*-
import ave
#from modulos.animales import zoo
from modulos.animales import * #no recomendable

def alguna_funcion():
	return "El veloz murciélago hindú"

if __name__ == "__main__":
	#sentencia para pruebas
	print zoo()
	c = ave.Ave('grande')
	b = ave.Ave('chica')
	b.volar(7)
	print alguna_funcion()