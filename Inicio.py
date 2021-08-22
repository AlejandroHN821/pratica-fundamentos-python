#Pedir y mostrar un nombre
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}")

#if

edad = input("¿Cual es tu edad?: ")
edad=int(edad)

if edad >=18 and edad <=120:
    print("Eres mayor de edad")
elif edad <=0:
    print("No existes")
else:
    print("¿Eres inmortal?")

#for

for i in range(0,5):
    print(i)
