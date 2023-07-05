#ejercicio 1

#pedir nombre y numero
nombre=str(input("Bienvenido por favor ingrese su nombre: "))
numero=int(input("Estimado/a " + nombre + " por favor ingrese un numero: "))
#contador
x=0
#cantidad de veces que se imprime
while( x < numero):
    print(nombre)
    x+=1
#otra forma sin ciclos
print("---forma 2---")
print((nombre + "\n") * numero)    
