#son tipos de datos que permiten almacenar varios tipos de datos
# se definen con [] y una , para separarlos

lista = [2,3,9,4,7,6]
lista2 = [3,"dfdsdf",2, True,[1,2,4]]
lista_3 = [
    2,
    4,
    5,
    True
]
#las listas se pueden modificar

print(lista[0])

lista[0] = 6 #cambiar el valor de la posicion 0 de la lista
print(lista[0])
print(lista)

#saber la longitud de una lista
print(len(lista)) 

#agregar elemento al final de la lista
lista.append(6)
print(lista)

#Eliminar el ultimo elemento 
lista.pop()
print(lista)

#eliminar un elemento en concreto con su indice
lista.remove(6)
print(lista)

#elimina todos los elementos de una lista
lista.clear()
print (lista)

#cuantas veces se repite un elemento
lista3=[6,8,7,6,6,3,2,1]
print(lista3.count(6))