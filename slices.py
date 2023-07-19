#slices
#[inicio: fin: saltos]
nombre= "Francisco"

#posicion de un caracter en el nombre // siempre parte de 0
print(nombre[0])
print(nombre[3])

#Fra
print(nombre[0:2]) #elegir la posicion desde donde seleccionara los caracteres : avanzara segun lo plateado

print(nombre[0:3])

print(nombre[3:]) #parte desde la posicion indicada y por defecto avanzara hasta el final si no hay nada despues del :

#rancis
print(nombre[1:7])

#rni //hacer saltos (cuenta dos y toma el siguiente, parte desde el ultimo que tomo )
print(nombre[1:7:2]) 

#Francisco
print(nombre[::3]) #por defecto parte del principo : llega al fin : salta en 1

#rcc
print(nombre[1::3])

#el nombre al reves (en el salto usar negativo para ir de derecha a izquierda)
print(nombre[::-1])


