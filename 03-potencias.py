def potencias (base, limite):
    i = 1
    a = 1
    while a < limite:
        print(a)
        a = base ** i
        i += 1


def run():
    print("Potencias!")
    base = int(input("Inserte el número del que quiere hallar potencias:"))
    limite = int(input("Inserte el límite máximo: "))
    potencias(base, limite)

if __name__ == "__main__":
    run()