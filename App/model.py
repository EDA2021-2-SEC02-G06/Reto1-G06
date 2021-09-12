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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo que contiene listas y obras. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras. 
    Retorna el catalogo inicializado.
    """
    catalog = {'artist': None,
               'obras': None,
               }

    catalog['artist'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=None)
    catalog['obras'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=None)

    return catalog

def artistalista():

    retorno = {'artist': None}
    retorno['artist'] = lt.newList('SINGLE_LINKED', cmpfunction=None)
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
    
    lt.addLast(catalog['obras'], obras) 

  



# Funciones para creacion de datos

# Funciones de consulta

def getLastArtist(catalog):
    """
    Retorna la lista con los últimos tres artistas de la lista de 
    artistas.
    """
    artistas = catalog['artist']
    lastartist = []
    num = lt.size(catalog["artist"])
    i = 0
    while i < 3:
        ultimos = num - i
        book = lt.getElement(artistas, ultimos)
        lastartist.append(book)
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

# Funciones utilizadas para comparar elementos dentro de una lista



# Funciones de ordenamiento