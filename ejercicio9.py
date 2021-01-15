"""un programa que pida dos números por teclado y devolver el número más alto de los dos
introducidos
"""

num1=int(input("Introduce el primer valor:\n"))
num2=int(input("Introduce el segundo valor:\n"))

print("El resultado es:")

if num1 >num2:
    print(num1)

elif num1<num2:
    print(num2)

else:
    print("Son iguales")
