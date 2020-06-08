#Estrategia incremental
#Algoritmo de ordenacion por insercion
'''
21 10 12 0 34 15
Parte ordenada 
21                  10 12 0 34 15
10 21               12 0 34 15
10 12 21            0 34 15
0 10 12 21          34 15
0 10 12 21 34       15
0 10 12 15 21 34 
'''

def insertSort(lista):
    for index in range(1, len(lista)):
        actual = lista[index]
        posicion = index
        #print("Valor a ordenar {}".format(actual))
        while posicion > 0 and lista[posicion-1] > actual:
            lista[posicion] = lista[posicion-1]
            posicion = posicion-1
        lista[posicion] = actual
        #print(lista)
        #print()
    return lista

lista = [21, 10, 12, 0, 34, 15]
#print(lista)
insertSort(lista)
#print(lista)

