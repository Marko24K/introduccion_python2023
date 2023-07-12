#nombres de las funciones siguen la misma reglas de las variables
def imprimir():
    print("hola karlita")
    print("hola")

imprimir()
def saludo( nombre = "Juan", apellido = "Gonzales"):
    print("hola " + nombre +" "+ apellido)


saludo() #si no hay valores por defecto toma los que fueron definidos en la funcion
saludo("Nigerio")
saludo("Sancho")
saludo("Sancho", "panza")
saludo(apellido = "lagos", nombre="mar") #se debe poner el nombre de la variable si van en distinto orden
