#Implementar una función que reciba una lista y devuelva la suma de los valores de la lista
numeros = [2, 5, 4, 6, 3, 6, 4, 24, 76, -100]

def sumaLista(list):
    suma = 0
    for i in list: 
        suma = suma + i

    return suma

print("Suma de la lista ", sumaLista(numeros))

#Implementar una función que reciba una lista y devuelva la lista inversa de la lista

def invertirLista(list):
    newList = []
    listRange = len(list)
    for i in range(len(list)):     
        #newList.insert(i, list[listRange - 1])
        newList.append(list[listRange - 1])
        listRange = listRange - 1

    print("Lista al reves", newList)
    
invertirLista(numeros)