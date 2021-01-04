# validar si un email contiene "@" y "."
contador=0
mi_email=input("Introduce tu dirrecion de email")
for i in mi_email:
    if i=="@" or i==".":
        contador +=1
    
if contador==2:
    print("El email es correcto")
else:
    print("El email es incorrecto")
