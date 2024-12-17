miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid"}

print(miDiccionario["Francia"])
print(miDiccionario["España"])

print("imprimir todo", miDiccionario)

#Agregar
miDiccionario["Italia"] = "Lisboa"
print("Erroneo",miDiccionario["Italia"])
miDiccionario["Italia"] = "Roma"
print("Corregido",miDiccionario["Italia"])

#Borrar
del miDiccionario["Francia"]
print("Con el borrado", miDiccionario)

miTupla = ("España", "Alemania", "Italia")
miDiccionario = {miTupla[0]:"Madrid", miTupla[1]:"Berlin", miTupla[2]:"Roma"}
print(miDiccionario)
print("Devolver claves",miDiccionario.keys())
print("Devolver valores",miDiccionario.values())
print("Longitud diccionario", len(miDiccionario))


#Implementar una función que reciba una lista de tuplas y devuelva un diccionario donde las claves son los primeros elementos de las tuplas y los valores una lista con los segundos elementos
tupla1 = ("uno", "dos", "tres")
tupla2 = (1, 2, 3)

lista = [tupla1, tupla2]
diccionario = {}

def joinTuplaLista(miLista):
    #Iteramos utilizando zip para emparejar las claves y valores
    for clave, valor in zip(miLista[0], miLista[1]):
        diccionario[clave] = valor
        #print(diccionario)

joinTuplaLista(lista)
print(diccionario)


#Implementar una función que reciba una cadena y devuelva un diccionario con la cantidad de repeticiones de cada palabra en la cadena
import re

oracion = "Implementar una función que reciba una Cadena, y devuelva un \ndiccionario? con la cantidad de repeticiones de cada palabra. en la cadena"

def countPalabras(cadena):
    #
    cadena = re.sub(r'[^\w\s]', '', cadena).lower()
    palabras = cadena.split()

    contadorDiccionario = {}
    
    for palabra in palabras:
        if palabra in contadorDiccionario:
            contadorDiccionario[palabra] += 1
        else:
            contadorDiccionario[palabra] = 1
    
    return contadorDiccionario

print(countPalabras(oracion))
        



