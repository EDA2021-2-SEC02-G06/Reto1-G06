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
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artist': None,
               'obras': None,
               }

    catalog['artist'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=None)
    catalog['obras'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=None)

    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, book):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artist'], book)
 
def addObras(catalog, book):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['obras'], book)   

def getLastArtist(catalog):
    """
    Retorna los mejores libros
    """
    artistas = catalog['artist']
    lastartist = lt.newList()
    num = lt.size(catalog["artist"])

    i = 0
    while i < 2:
        book = lt.getElement(artistas, num-i)
        lt.addLast(lastartist, book)
        i += 1
    
    return lastartist 

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento