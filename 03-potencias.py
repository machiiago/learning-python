def potencias (base, limite):
    i = 0
    a = 0
    while a < limite:
        a = base ** i
        print (a)
        i += 1


def run():
    print("Potencias!")
    base = int(input("Inserte el número del que quiere hallar potencias:"))
    limite = int(input("Inserte el límite máximo: "))
    potencias(base, limite)

if __name__ == "__main__":
    run()