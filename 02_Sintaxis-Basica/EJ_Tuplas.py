import random

#Implementar una representación con tuplas de la baraja francesa
def barajaCreate():
    figuras = ('♥', '♦', '♣', '♠')
    cartas = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

    barajaFrancesa = [(figura, carta) for figura in figuras for carta in cartas]
    return barajaFrancesa

baraja = barajaCreate()

#print(baraja[3])
#for carta in baraja:
   # print(carta)


#Implementar una función que reciba circo cartas de la baraja francesa y devuelva si tiene un poker o no (4 cartas con el mismo número)

def poker(mano):
    #Extraemos el valor de las cartas de la mano carta[1] porque los valores estan en la segunda posicion
    valores = [carta[1] for carta in mano]

    #Aqui con set(valores) recorremos cada valor sin duplicados y los contamos
    for valor in set(valores):
        if valores.count(valor) == 4:
            return True

    return False

mano_poker = random.sample(baraja, 5)
print("Mano aleatoria:", mano_poker)

if poker(mano_poker):
    print("POKER")
else:
    print("NO HAY POKER :(")
