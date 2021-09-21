"""
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
from datetime import datetime as dt
from DISClib.ADT import list as lt

assert cf
default_limit = 1000
sys.setrecursionlimit(default_limit*30)

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

def muestra():
    numero = int(input("Ingrese el tamaño de la muestra :"))
    return numero

def algoritmo():
    print("A continuación las opciones de algoritmos de ordenamiento que puede usar:")
    print("1. Insertion Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Shell Sort")
    
    algoritmo = int(input("Seleccione el tipo de algoritmo que desea usar:"))
    if algoritmo == 1:
        algoritmo = "InsertionSort"
        return algoritmo
    
    if algoritmo == 2:
        algoritmo = "MergeSort"
        return algoritmo
    
    if algoritmo == 3:
        algoritmo = "QuickSort"
        return algoritmo
    if algoritmo == 4:
        algoritmo = "ShellSort"
        return algoritmo

def opcionesLista():
    print("A continuación las opciones de lista que puede usar:")
    print("1. Linked List")
    print("2. Array List")
    tipo = int(input("Seleccione el tipo de lista que desea usar:"))
    if tipo == 1:
        linked = "LINKED_LIST"
        return linked
    
    if tipo == 2:
        arreglo = "ARRAY_LIST"
        return arreglo

def initCatalog(tipo):
    """
    Llama a la función contenida en controller encargada de inicializar el catálogo de libros.
    """
    return controller.initCatalog(tipo)

def initArtistRetorno():
    return controller.initArtistCrono()

def initObrasRetorno():

    return controller.initObrasCrono()

def loadData(catalog):
    """
    Llama a la función contenida en controller encargada de cargar los datos.
    """
    controller.loadData(catalog)

def loadDataArtist(catalog,retorno,inicio,fin):

    controller.loadDataArtist(catalog,retorno,inicio,fin)

def loadDataObras(catalog,retorno,inicio,fin):

    controller.loadDataObras(catalog,retorno,inicio,fin)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo = opcionesLista()
        print(tipo)
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo)
        loadData(catalog)
        print("Artistas cargados: " + str(lt.size(catalog["artist"])))
        print("Obras cargadas: " + str(lt.size(catalog["obras"])))
        print("Últimos tres Artistas: " + str(controller.getLastArtist(catalog)))
        print("Últimas tres Obras: " + str(controller.getLastObras(catalog)))
        

    
    elif int(inputs[0]) == 2:

        añoinicio = int(input("Ingrese el año inicial:"))
        añofin = int(input("Ingrese el año final:"))
        artistlista = initArtistRetorno()
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
        fecha_inicio = (input("Ingrese la fecha inicial (AAAA-MM-DD):"))
        fecha_fin = (input("Ingrese la fecha final (AAAA-MM-DD):"))
        
        obralista = initObrasRetorno()
        loadDataObras(catalog,obralista,fecha_inicio,fecha_fin)

        numero_muestra = muestra()
        
        tipo_algoritmo = algoritmo()

        
        ordenada = controller.aplicarAlgoritmoObras(obralista,tipo_algoritmo)
        por_compra = controller.contarPorCompra(ordenada[1])

        print("El MoMa adquirió "+ str(lt.size(ordenada[1])) + " obras entre la fecha "+ fecha_inicio + " y " + 
        fecha_fin +" de las cuales compró "+ str(por_compra))
        

        ultimasobras= controller.getFirstObras_Dos(ordenada[1])
        primerasobras = controller.getLastObras_Dos(ordenada[1])

        print(ultimasobras)
        print(primerasobras)


        print("|        TITULO       | ID ARTISTA | FECHA |  MEDIO  |  DIMENSIONES  | ")
        i = 2
        while i != -1:

            if "," not in ((primerasobras[i]["ConstituentID"])):

                title = primerasobras[i]["Title"]
                artista = controller.EncontrarArtista(catalog,int(((primerasobras[i]["ConstituentID"]).replace("[","").replace("]","")))) 
                fecha = primerasobras[i]["Date"]
                medio = primerasobras[i]["Medium"]
                dimensiones = primerasobras[i]["Dimensions"]
                i -= 1
                print(" "+title+"        "+"     "+artista+"   "+"     "+fecha+"    "+"     "+medio+"   "+"     "+dimensiones)
                print("______________________________________________________")

        
        print("_ _ _ _ __ _ _ _ __ _ _ _ __ _ _ _ __ _ _ _ _-")

        for j in range(0,3):
            
            title = ultimasobras[j]["Title"]
            
            fecha = ultimasobras[j]["Date"]
            medio = ultimasobras[j]["Medium"]
            dimensiones = ultimasobras[j]["Dimensions"]
            if "," not in ultimasobras[j]["ConstituentID"]:
                constituent = controller.EncontrarArtista(catalog,int(((ultimasobras[j]["ConstituentID"]).replace("[","").replace("]",""))))
                print(" "+title+"        "+"     "+constituent+"   "+"     "+fecha+"    "+"     "+medio+"   "+"     "+dimensiones)
                print("______________________________________________________")
            else:
                constituent = ultimasobras[j]["ConstituentID"]
                print(" "+title+"        "+"     "+constituent+"   "+"     "+fecha+"    "+"     "+medio+"   "+"     "+dimensiones)
                print("______________________________________________________")


        print("Tiempo de ejecución : " + str(ordenada[0]))

       

       

    
        
    

    elif int(inputs[0]) == 4:
    
        nom = input("¿Cuál es el nombre del artista?: ")
        Id_A = controller.EncontrarArtista2(nom, catalog)
        ObrasNom = controller.ObrasPorArtista(Id_A, catalog)
        print(nom + " con el ID en el MoMa número " + str(Id_A) + " tiene " + str(ObrasNom) + " a su nombre en el museo.")
        dictReq4 = controller.ListaDictReq4(catalog, Id_A)
        cantidad = len(dictReq4)
        print("Existen " + str(cantidad) + " distintas técnicas en su trabajo artistico")
        print("Su técnica más utilizda es: " + dictReq4[0]["metodo"] + " con " + str(dictReq4[0]["numero"]) + " piezas")
        print("Unos datos de las " + str(dictReq4[0]["numero"]) + " obras realizadas con " + dictReq4[0]["metodo"] + "se ve a continuación:")
        RecapTecnicaObras = controller.RecapTecnicaObras(catalog, dictReq4)
        print("|          TITULO         |   ID OBJETO   |      FECHA      |       MEDIO       |       DIMENSIONES       | ")
        for element in RecapTecnicaObras:
            print(element["titulo"] + " | " + element["id"] + " | " + element["fecha"] + " | " + element["tecnica"]+ " | " + element["dimensiones"])
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")


    elif int(inputs[0]) == 5:
        pass
    
    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
