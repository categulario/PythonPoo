#experimento con la API de twitter

import urllib
import json

def buscarTweets(cadena):
    busqueda = urllib.urlopen('http://search.twitter.com/search.json?q='+cadena)
    diccionario = json.loads(busqueda.read())
    for tweet in diccionario['results']:
        print "----------"
        print "*", tweet["text"]

if __name__ == "__main__":
    print buscarTweets('python')
