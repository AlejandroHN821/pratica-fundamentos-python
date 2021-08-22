# Libreria para generar datos aleatorios
import random

# Libreria para generar graficas
import matplotlib.pyplot as plt

# Generar un numero aleatorio -> randint, randrange
print(random.randrange(10,100,2))

# Reacomodar una lista al azar
lista=[1,2,3,4,5,6,7,8,9,10]
print('Lista original', lista)

random.shuffle(lista)
print('Lista mixeada',lista)

# Generar campana de gauss
campana=[random.gauss(1,0.5) for i in range(1000)]      # Genera los datos de la grafica
plt.hist(campana, bins=15)                              # Arma la grafica
plt.show()