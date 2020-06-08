import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from time import time 
from ejercicio5 import insertSort
from ejercicio6 import quicksort

datos = [ii+100 for ii in range(1,21)]
tiempo_is = []
tiempo_qs = []
for ii in datos:
    lista_is = random.sample(range(0,10000000), ii)
    lista_qs =lista_is.copy()

    t0 = time()
    insertSort(lista_is)
    tiempo_is.append(round(time()-t0,6))

    t0 = time()
    quicksort(lista_qs)
    tiempo_qs.append(round(time()-t0,6))
    
print("Tiempos parciales de ejecucion en inserSort {}[s]".format(tiempo_is))
print("Tiempos parciales de ejecucion en quicksort {}[s]".format(tiempo_qs))

fig, ax = plt.subplots()
ax.plot(datos, tiempo_is, label="inserSort", marker="*", color ="r")
ax.plot(datos, tiempo_qs, label="quicksort", marker="o", color ="b")

ax.set_xlabel("Datos")
ax.set_ylabel("Tiempo")
ax.grid(True)
ax.legend(loc=2)

plt.title("Tiempos de ejecucion [s] inserSort vs quicksort")
plt.show()