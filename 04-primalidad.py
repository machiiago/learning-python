def es_primo(num):
    limite = int(num ** 0.5) + 1
    testigo = False
    for i in range(2,limite):
        if num % i == 0:
            Testigo = True
    if Testigo:
        print("El número no es primo")
    else:
        print("El número es primo")

def run():
    print("¡Prueba de primalidad")
    numero = int(input("Inserte un número"))
    es_primo(numero)

if __name__ == "__main__":
    run()