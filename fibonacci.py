
n=int(input(" Introduce un numero entero:\n"))
fibonacci=1
ultimo_num=0
anterior=0
posicion=1

while posicion < n:
    anterior= ultimo_num
    ultimo_num=fibonacci
    fibonacci=anterior+ultimo_num
    posicion+=1

print(f"Fibonacci({posicion}) = {fibonacci}")
