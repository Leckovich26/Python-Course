        # miDoc=requests.get("https://python.beispiel.programmierenlernen.io/") #Guarda toda la pagina web en esa variable.

        # docFinal= BeautifulSoup(miDoc.text, "html.parser") #aqui guardo todo el texto que tiene esa pagina, convierte el contenido HTML en un objeto BeautifulSoup para poder navegarlo y buscar elementos

        # self.titulo= docFinal.select(".card-title span") # Selecciona todos los elementos que tengan la clase "emoji" y los guarda en una lista

        # self.texto= docFinal.select(".card-text") # Selecciona todos los elementos con la clase "card-text" y los guarda en una lista

        # for imagen in docFinal.select(".card-block img"):  # Recorre todas las etiquetas <img> dentro de elementos con clase "card-block"

        #     print(imagen.attrs["src"])

from bs4 import BeautifulSoup 

import requests 

from urllib.parse import urljoin

import time

import csv

class CrawlerPost():

    def __init__(self, emoji, titulo, texto, imagen):

        self.emoji=emoji
        self.titulo=titulo
        self.texto=texto
        self.imagen=imagen
        
class PostExtractor():

    def extractor(self):

        urlbase= "https://python.beispiel.programmierenlernen.io/"

        post=[]

        while urlbase!="":

            miDoc=requests.get(urlbase) 

            docFinal= BeautifulSoup(miDoc.text, "html.parser") 

            time.sleep(2)

            for card in docFinal.select(".card"):
                
                titulo=card.select(".card-title span")[1].text
                emoticono=card.select_one(".emoji").text
                contenido=card.select_one(".card-text").text
                imagen=urljoin(urlbase, card.select_one("img").attrs["src"])

                crawled=CrawlerPost(emoticono,titulo,contenido,imagen)
                post.append(crawled)
                
                yield CrawlerPost(titulo, emoticono, contenido, imagen)

            boton_siguiente=docFinal.select_one(".navigation .btn")

            if boton_siguiente:
                rutas_absolutas=urljoin(urlbase, boton_siguiente.attrs["href"])
                urlbase=rutas_absolutas
                print(rutas_absolutas)
                
            else:
                urlbase=""

        return post
    
posti=PostExtractor()

listapost=posti.extractor()

contador=0 
for i in listapost:

    if contador==12:
        break
    contador+=1 

    print(i.emoji)
    print(i.titulo)
    print(i.texto)
    print(i.imagen)
    print()

# with open("Crawler Info.csv", "w", newline='', encoding='utf-8') as csvfile:
#     Postwriter= csv.writer(csvfile, delimiter=',',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     for mipost in posti.extractor():
#         Postwriter.writerow([mipost.emoji, mipost.titulo, mipost.texto, mipost.imagen])
    
    
    
  