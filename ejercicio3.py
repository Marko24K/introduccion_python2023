# cuantos payasos y muñecas se venden
payasos=int(input("Ingrese cantidad vendida de payasos: "))
munecas=int(input("Ingrese cantidad vendida de muñecas: "))

#pesos en g
peso_paya = 112
peso_mune = 75

#calculo
total= (payasos * peso_paya) + (munecas * peso_mune)
print(f"El peso total del contenido es: {total} gramos")
