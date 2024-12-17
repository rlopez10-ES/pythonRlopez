#Implementar una función que reciba tres números y devuelva el máximo de tres valores

num1 = int(input("Introduce un numero "))
num2 = int(input("Introduce un segundo numero "))
num3 = int(input("Introduce un tercer numero "))

nums = [num1, num2, num3]

def higherNum(n1, n2, n3):
    if n1>n2:
        if n1>n3:
            return n1
        elif n2>n3:
            return n2
        else:
            return n3
    else:
        if n2>n3:
            return n2
        else:
            return n3

print(higherNum(num1, num2, num3))


#otra forma


def higherNum2(numeros):
    max_vle = numeros[0]
    
    for i in numeros:
        if i > max_vle:
            max_vle = i

    return max_vle

print(higherNum2(nums))

#otra forma
def higherNum3(numeros):
    return max(numeros)

print(higherNum3(nums))


#Implementar una función que reciba un carácter y devuelva si el carácter es una vocal

palabra = input("Introduce una palabra ")
def isVocal(voc):
    response = False
    for c in voc:
        if c in "aeiouAEIOU":
            response = True
    return response

if isVocal(palabra):
    print("Hay vocales")
else:
    print("No hay vocales en la palabra")
    
