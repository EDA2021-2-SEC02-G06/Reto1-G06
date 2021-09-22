"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from datetime import datetime as dt
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import shellsort as sh
from operator import itemgetter
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):
    """
    Inicializa el catálogo que contiene listas y obras. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras. 
    Retorna el catalogo inicializado.
    """
    catalog = {'artist': None,
               'obras': None,
               }

    catalog['artist'] = lt.newList(tipo,
                                    cmpfunction=None)
    catalog['obras'] = lt.newList(tipo,
                                    cmpfunction=None)

    return catalog

def artistalista():

    retorno = {'artist': None}
    retorno['artist'] = lt.newList('ARRAY_LIST', cmpfunction=None)
    return retorno

def obralista():

    retorno = {'obras': None}
    retorno['obras'] = lt.newList('ARRAY_LIST', cmpfunction=None)
    return retorno


# Funciones para agregar informacion al catalogo
def addArtist(catalog, artista):
    """
    Función encargada de añadir los artistas a la lista de artistas en el catalogo.
    """
    
    lt.addLast(catalog['artist'], artista)
 
def addObras(catalog, obras):
    """
    Función encargada de añadir las obras a la lista de obras en el catalogo.
    """
    if obras["DateAcquired"] == "" or obras["DateAcquired"] == "Unknown":
        hoy = dt.today()
        obras["DateAcquired"] = hoy.strftime("%Y-%m-%d")

    lt.addLast(catalog['obras'], obras) 

  
def ListaNacionalidades(catalog):

    nacionalidades = lt.newList("ARRAY_LIST",cmpfunction=None,)

    for artist in lt.iterator(catalog):
        nacionalidad = int(artist["BeginDate"])
        if (año>=inicio) and (año <= fin) and (año != None):
            model.addArtist(retorno,artist)

def ContarPaises(catalog):


    interno = lt.newList("ARRAY_LIST",cmpfunction=None)
    lt.addLast(interno,"Unknown")

    for artist in lt.iterator(catalog["artist"]):
        if not(lt.isPresent(interno,artist["Nationality"])):

            lt.addLast(interno,artist["Nationality"])
            

            
            
    return interno




    for artist in lt.iterator(catalog["artist"]):
        if artist["Nationality"] in interno:
            interno[artist["Nationality"]] +=1
        elif artist["Nationality"] == ""  :
            interno["Unknow"] += 1
            
    return interno
   

         

    


# Funciones para creacion de datos
def sublista(lista,tamaño):
    lista_dos = lista["obras"]

    return lt.subList(lista_dos,1,tamaño)

# Funciones de consulta
def getFirstArtist(catalog):
    """
    Retorna la lista con los últimos tres artistas de la lista de 
    artistas.
    """
    artistas = catalog['artist']
    firstartist = lt.newList("ARRAY_LIST",cmpfunction=None)
    num = lt.size(catalog["artist"])
    i = 0
    while i < 3:
        ultimos = i
        artista = lt.getElement(artistas, ultimos)
        lt.addLast(firstartist,artista)
        i += 1
    
    return firstartist 

def getLastArtist(catalog):
    """
    Retorna la lista con los últimos tres artistas de la lista de 
    artistas.
    """
    artistas = catalog['artist']
    lastartist = lt.newList("ARRAY_LIST",cmpfunction=None)
    num = lt.size(catalog["artist"])
    i = 0
    while i < 3:
        ultimos = num - i
        book = lt.getElement(artistas, ultimos)
        lt.addLast(lastartist,book)
        i += 1
    
    return lastartist 

 

def getLastObras(catalog):
    """
    Retorna la lista con las últimas tres obras de la lista de 
    artistas.
    """
    
    artworks = catalog['obras']
    lastobras = []
    num = lt.size(catalog["obras"])
    i = 0
    while i < 3:
        ultimos = num - i
        book = lt.getElement(artworks, ultimos)
        lastobras.append(book)
        i += 1
    
    return lastobras

def getFirstObras_Dos(catalog):
    """
    Retorna la lista con los últimos tres artistas de la lista de 
    artistas.
    """
    artistas = catalog
    firstartist = []
    
    i = 3
    while i != 0:
        ultimos = i
        artista = lt.getElement(artistas, ultimos)
        firstartist.append(artista)
        i -= 1
    
    return firstartist

def getLastObras_Dos(catalog):
    """
    Retorna la lista con las últimas tres obras de la lista de 
    artistas..
    """
    
    artworks = catalog
    lastobras = []
    num = lt.size(catalog)
    i = 2
    while i != -1:
        ultimos = num - i
        book = lt.getElement(artworks, ultimos)
        lastobras.append(book)
        i -= 1
    
    return lastobras

def EncontrarArtista(catalogo,codigo):

    for artist in lt.iterator(catalogo["artist"]):
        
        if int(artist["ConstituentID"]) == codigo:
            
            return artist["DisplayName"]
def EncontrarArtistaByNacionality(catalogo, codigo):

    for artist in lt.iterator(catalogo["artist"]):
        
        if int(artist["ConstituentID"]) == codigo:
            
            return artist["Nacionality"]


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtistByDate(artist1, artist2):

    return artist1["BeginDate"] < artist2["BeginDate"]


def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return dt.fromisoformat(artwork1["DateAcquired"]) > dt.fromisoformat(artwork2["DateAcquired"])

def cmpArtworkByDate(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'Date' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return dt.fromisoformat(artwork1["Date"]) < dt.fromisoformat(artwork2["Date"])

# Funciones de ordenamiento

def MergeSort(lista,cmpfunction):
    start_time = time.process_time()
    sorted_list = ms.sort(lista,cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg,sorted_list
    
    

def InsertionSort(lista,cmpfunction):
    start_time = time.process_time()
    sorted_list = si.sort(lista,cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg,sorted_list

def ShellSort(lista,cmpfunction):
    start_time = time.process_time()
    sorted_list = sh.sort(lista,cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg,sorted_list

def QuickSort(lista,cmpfunction):
    start_time = time.process_time()
    sorted_list = qs.sort(lista,cmpfunction)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg,sorted_list

def EncontrarArtista2(nom, catalogo):

    for artist in lt.iterator(catalogo["artist"]):
        if nom in artist["DisplayName"]:
            return artist["ConstituentID"]

def ObrasPorArtista(Id_A, catalogo):
    lcod = []
    for obra in lt.iterator(catalogo["obras"]):
        if "," in obra["ConstituentID"]:
            var = obra["ConstituentID"]
            var = var.split()
            for e in var:
                lcod.append(e)
        else:
            lcod.append(obra["ConstituentID"].replace("[","").replace("]",""))


    i = 0
    for obras in lcod:
        if Id_A == obras:
            i += 1
    return i 

def ListaDictReq4(catalogo, Id_A):
    Ldr4 = []
    #Ldr4.append({"metodo": "Zr", "numero": 0})
    for obra in lt.iterator(catalogo["obras"]):
        dicit = {"metodo": obra["Medium"], "numero": 1, "obras": [obra["ObjectID"]]}
        if "," in obra["ConstituentID"]:
            var = obra["ConstituentID"]
            var = var.split()
            for e in var:
                if Id_A == e:
                    f = True
                    for a in Ldr4:
                        if a["metodo"] == obra["Medium"]:
                            a["numero"] += 1
                            a["obras"].append(obra["ObjectID"])
                            f = False
                    if f == True:
                        Ldr4.append(dicit)
        
        else:
            if Id_A == obra["ConstituentID"].replace("[","").replace("]",""):
                    f = True
                    for r in Ldr4:

                        if r["metodo"] == obra["Medium"]:
                            r["numero"] += 1
                            r["obras"].append(obra["ObjectID"])
                            f = False
                    if f == True:
                        Ldr4.append(dicit)
                        
    

    Ldr4 = sorted(Ldr4, key=itemgetter('numero'), reverse=True)
    return Ldr4

def RecapTecnicaObras(catalog, dictReq4):  
    LGrande = []
    miniL = []
    for a in dictReq4[0]["obras"]:
        miniL.append(a)

        

    for obra in lt.iterator(catalog["obras"]):
        for ob in miniL:

            if obra["ObjectID"] == ob:
                dicto = {"titulo": obra["Title"], "id": obra["ObjectID"], "fecha": obra["Date"], "tecnica": obra["Medium"], "dimensiones": obra["Dimensions"]}
                LGrande.append(dicto)
        
    return LGrande 
    