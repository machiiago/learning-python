def prueba(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra2 = palabra[::-1]
    resultado = palabra == palabra2
    return resultado
hola = "asdf"


def run():
    print("¿Es palindromo o no?")
    palabra = input("Inserte palabra o frase: ")
    es_palindromo = prueba(palabra)
    if es_palindromo == True:
        print ("Es palíndromo")
    else:
        print ("No es palíndromo")


if __name__ == "__main__":
    run()