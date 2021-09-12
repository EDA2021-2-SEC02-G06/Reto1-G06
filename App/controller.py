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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo.
    """
    catalog = model.newCatalog()
    return catalog

def initArtistCrono():
    """
    Llama la función que crea una lista vacía para el requerimiento 1.
    """
    retorno = model.artistalista()
    return retorno

# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtist(catalog)
    loadObras(catalog)

def loadDataArtist(catalog,retorno,inicio,fin):
    loadCronoArtist(catalog,retorno,inicio,fin)

def loadArtist(catalog):
    """
    Carga los artistas del archivo. Se carga el CSV en una variable, posteriormente 
    se lee el archivo y se cicla para añadir el artista a una lista con la llamada a
    la función addArtist.
    """
    artistfile = cf.data_dir + 'MOMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistfile, encoding='utf-8'))
    for artista in input_file:
        model.addArtist(catalog, artista)

def loadObras(catalog):
    """
    Carga las obras del archivo. Se carga el CSV en una variable, posteriormente 
    se lee el archivo y se cicla para añadir la obra a una lista con la llamada a
    la función addObras.
    """
    obrasfile = cf.data_dir + 'MOMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(obrasfile, encoding='utf-8'))
    for obra in input_file:
        model.addObras(catalog, obra)

def loadCronoArtist(catalog,retorno,inicio,fin):
    
    for artist in catalog["artist"]["elements"]:
        año = int(artist["BeginDate"])
        if (año>=inicio) and (año <= fin) and (año != None):
            model.addArtist(retorno,artist)
    
    
    print(inicio)
    print(fin)
        
        
        

# Funciones de ordenamiento



# Funciones de consulta sobre el catálogo

def getLastArtist(catalog):
    """
    Llama a la función getLastArtist de model y retorna los valores de la misma
    en una variable.
    """
    lastartist = model.getLastArtist(catalog)
    return lastartist

def getLastObras(catalog):
    """
    Llama a la función getLastObras de model y retorna los valores de la misma
    en una variable.
    """
    lasobras = model.getLastObras(catalog)
    return lasobras



