import random
RESPUESTA = random.randint(1, 100)
bienvenida = """Bienvenido a:
ADIVINA EL NÚMERO
La computadora escogerá un número al azar entre 1 y 100
¿Podrás adivinarlo?
*psss... si estás a 5 números o menos te avisaré"""
VICTORIA = """Hallaste el número!!
Número de intentos: """
banco = ["menor que ese", "mayor que ese", "... ¡Pero estás cerca!", ""]


def diferencia(numero):
    if abs(RESPUESTA - numero) < 6:
        cerca = 2
    else:
        cerca = 3
    if RESPUESTA - numero > 0:
        may_men = 1
    else:
        may_men = 0
    print("El número que buscas es " + banco[may_men] + banco[cerca])
    

def run():
    print(bienvenida)
    numero = int(input("Escoge un número: "))
    contador = 1
    while numero != RESPUESTA:
        diferencia(numero)
        numero = int(input("Escoge otro número: "))
        contador += 1
    print(VICTORIA + str(contador))



if __name__ == "__main__":
    run()