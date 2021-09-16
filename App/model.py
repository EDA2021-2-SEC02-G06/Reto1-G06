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
from datetime import datetime as dt
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as si
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import shellsort as sh
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

  



# Funciones para creacion de datos

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
    firstartist = lt.newList("ARRAY_LIST",cmpfunction=None)
    num = lt.size(catalog)
    i = 0
    while i < 3:
        ultimos = i
        artista = lt.getElement(artistas, ultimos)
        lt.addLast(firstartist,artista)
        i += 1
    
    return firstartist

def getLastObras_Dos(catalog):
    """
    Retorna la lista con las últimas tres obras de la lista de 
    artistas..
    """
    
    artworks = catalog
    lastobras = []
    num = lt.size(catalog)
    i = 0
    while i < 3:
        ultimos = num - i
        book = lt.getElement(artworks, ultimos)
        lastobras.append(book)
        i += 1
    
    return lastobras

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return dt.fromisoformat(artwork1["DateAcquired"]) < dt.fromisoformat(artwork2["DateAcquired"])


# Funciones de ordenamiento

def MergeSort(lista,cmpfunction):
    return ms.sort(lista,cmpfunction)

def InsertionSort(lista,cmpfunction):
    return si.sort(lista,cmpfunction)

def ShellSort(lista,cmpfunction):
    return sh.sort(lista,cmpfunction)

def QuickSort(lista,cmpfunction):
    return qs.sort(lista,cmpfunction)