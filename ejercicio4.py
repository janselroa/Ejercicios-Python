# un programa en Python que nos permita conocer todas las vocales que existen dentro de una palabra.


sentencia = input("Ingresa una palabra:\n")
vocales = ""
for i in sentencia:
    if i in ["a", "e", "i", "o", "u"]:
        vocales=vocales+i

print(vocales)