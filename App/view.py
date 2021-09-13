﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras según la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")
    print("8- Salir")

def initCatalog():
    """
    Llama a la función contenida en controller encargada de inicializar el catálogo de libros.
    """
    return controller.initCatalog()

def initRetorno():
    return controller.initArtistCrono()

def loadData(catalog):
    """
    Llama a la función contenida en controller encargada de cargar los datos.
    """
    controller.loadData(catalog)

def loadDataArtist(catalog,retorno,inicio,fin):

    controller.loadDataArtist(catalog,retorno,inicio,fin)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print("Artistas cargados: " + str(lt.size(catalog["artist"])))
        print("Obras cargadas: " + str(lt.size(catalog["obras"])))
        print("Últimos tres Artistas: " + str(controller.getLastArtist(catalog)))
        print("Últimas tres Obras: " + str(controller.getLastObras(catalog)))
    
    elif int(inputs[0]) == 2:

        añoinicio = int(input("Ingrese el año inicial:"))
        añofin = int(input("Ingrese el año final:"))
        artistlista = initRetorno()
        loadDataArtist(catalog,artistlista,añoinicio,añofin)
        primerosartistas = controller.getFirstArtist(artistlista)
        ultimosartista = controller.getLastArtist(artistlista)


        print("Número total de artista en el rango "+str(añoinicio)+" - "+str(añofin)+": " + str(lt.size(artistlista["artist"])))
        print("Primeros tres artistas en rango cronológico : ")
        
        
        print("|        NOMBRE        | AÑO DE NACIMIENTO | AÑO DE FALLECIMIENTO |  NACIONALIDAD  |  GÉNERO  | ")
        for i in range(0,3):
            name =primerosartistas["elements"][i]["DisplayName"]
            begin = primerosartistas["elements"][i]["BeginDate"]
            death = primerosartistas["elements"][i]["EndDate"]
            nacio = primerosartistas["elements"][i]["Nationality"]
            genero = primerosartistas["elements"][i]["Gender"]
            print(" "+name+"        "+"     "+begin+"   "+"     "+death+"    "+"     "+nacio+"   "+"     "+genero)

        for i in range(0,3):
            name =ultimosartista["elements"][i]["DisplayName"]
            begin = ultimosartista["elements"][i]["BeginDate"]
            death = ultimosartista["elements"][i]["EndDate"]
            nacio = ultimosartista["elements"][i]["Nationality"]
            genero = ultimosartista["elements"][i]["Gender"]
            print(" "+name+"        "+"     "+begin+"   "+"     "+death+"    "+"     "+nacio+"   "+"     "+genero)
    
    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass
    
    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
