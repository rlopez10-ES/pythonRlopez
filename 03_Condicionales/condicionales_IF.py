import random

#nota = random.randint(1, 10)
nota_usuario = int(input("Introduce una nota manualmente: "))

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    elif 5 < nota <= 10:
        valoracion = "aprobado"
    else:
        valoracion = "nota no valida"
    return valoracion

print(nota_usuario, evaluacion(nota_usuario))

edad_usuario = int(input("Introduce tu edad: "))

def permiso(edad):
    if 0 < edad < 18:
        print("no puedes pasar")
    elif edad > 150 or edad <= 0:
        print("edad incorrecta")
    else:
        print("puedes pasar")

permiso(edad_usuario)

#OPERADORES
distancia = int(input("Introduce la distancia a la que vives en KM: "))
hermanos = int(input("introduce el numero de hermanos: "))
salario = int(input("Introduce el salario anual de la unidad familiar: "))

if distancia > 40 and hermanos > 2 or salario <= 20000:
    print("BECA APROBADA")
else:
    print("No te corresponde BECA")


print("informatica - lengua - matematicas")
asignaturas = ["informatica", "lengua", "matematicas"]
asignatura = input("Introduce la asignatura preferida: ").lower()
if asignatura in(asignaturas):
    print("Asignatura elegida: " + asignatura)
else:
    print("asignatura no contemplada")