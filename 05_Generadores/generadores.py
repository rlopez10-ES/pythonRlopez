def generaPares(limite):
    numero = 1

    miLista = []

    while numero < limite:
        miLista.append(numero * 2)
        numero +=1

    return miLista

print(generaPares(10))


#AHORA LO MISMO PERO USANDO GENERADOR
def generaPares2(limite):
    numero = 1

    while numero < limite:
        yield numero * 2
        numero +=1

for i in generaPares2(10):
    print(i)
