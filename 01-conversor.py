#Mensaje de Bienvenida:
Bienvenida = """Bienvenido al conversor de monedas
Puede convertir entre las siguientes monedas:
1 Sol
2 Dólar
3 Peso chileno
4 Peso boliviano"""

#tupla con los cambios a dólar de: 1-sol, 2-dolar, 3-peso chileno y 4-peso boliviano:
cambio = [0.27, 1, 0.0014, 0.14]

#tupla con los nombres de las monedas:
monedas = ["soles", "dólares", "pesos chilenos", "pesos bolivianos"]

def conversion(moneda1, moneda2, monto):
    monto2 = monto*cambio[moneda2]/cambio[moneda1]
    return monto2

def run():
    print(Bienvenida)
    moneda1 = int(input("Inserte el número de la moneda desde la que quiere convertir: "))
    moneda2 = int(input("Inserte el número de la moneda a la que quiere convertir: "))
    monto = float(input("Inserte el monto que desea convertir: "))
    monto2 = conversion(moneda1, moneda2, monto)
    print("Usted tiene: " + str(monto2) + " " + monedas[moneda2])


if __name__ == "__main__":
    run()