def conversion (valor_dolar):
    valor=int(input("ingrese el valor a convertir: "))
    print("Su valor convertido es: $"+ str(round(valor/valor_dolar, 2)) )


print(""" 
Conversion de Monedas a dolares
1. pesos chilenos 
2. pesos mexicanos
3. pesos argentinos
      """)
opcion=int(input("opcion 1 Chileno 2 Mexicano 3 Argentino: "))
valor_mexicano = 17
valor_argen= 263
valor_chileno=797
"""
if opcion == 1:
    valor = int(input("ingrese un valor: "))
    conversion_chile=round (valor / valor_chileno , 2)
    print("Su valor en dolares es: $" +str(conversion_chile))
elif opcion == 2:
     valor = int(input("ingrese un valor: "))
     conversion_mexico=round(valor / valor_mexicano, 2)
     print("Su valor en dolares es: $" +str(conversion_mexico))
elif opcion == 3:
    valor = int(input("ingrese un valor: "))
    conversion_argentino = round(valor / valor_argen , 2)
    print("Su valor en dolares es: $" +str(conversion_argentino))

else:
    print("opcion invalida")"""
if opcion == 1:
    valor_chileno=797
    conversion(valor_chileno)

elif opcion == 2:
    valor_mexicano = 17
    conversion(valor_chileno)

elif opcion == 3:
    valor_argen= 263
    conversion(valor_chileno)


else:
    print("opcion invalida")