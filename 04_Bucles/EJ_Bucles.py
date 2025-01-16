#Implementar una función que reciba un numero y devuelva su descomposición en números primos
numero = int(input("Introduce un numero: "))


def descomposicion(num):
    numeros_des = []
    divisor = 2

    while num < 2:
        print("El numero debe ser mayor o igual a 2")
        num = int(input("Introduce un numero: "))

    while num > 1:
        while num % divisor == 0:
            numeros_des.append(divisor)
            num = num // divisor #numero //= divisor
        divisor += 1

    return numeros_des

print(descomposicion(numero))
    

#Implementar una función que reciba dos números y devuelva el máximo común divisor (Algoritmo de Euclides: https://es.wikipedia.org/wiki/Algoritmo_de_Euclides)
import math

numero1 = 105
numero2 = 300
print(math.gcd(numero1, numero2))

def maximoComunDivisor(num1, num2):
    numeroMayor = 0
    numeroMenor = 0
    if num1 > num2:
        numeroMayor, numeroMenor = num1, num2
    else:
        numeroMayor, numeroMenor = num2, num1

    # Si los números son iguales, el MCD es el número mismo
    if numeroMayor == numeroMenor:
        return numeroMayor
    
    maxcd = 0
    mincd = 2
    mincd2 = 2

    while numeroMayor != maxcd * mincd and numeroMenor != maxcd * mincd2:
        while numeroMenor % mincd2 != 0:
            mincd2 += 1
        maxcd = numeroMenor // mincd2

        if numeroMayor % maxcd != 0:
            mincd2 += 1
            continue

    return maxcd

print(maximoComunDivisor(numero1, numero2))




