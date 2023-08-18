"""conversion de pesos chilenos a dolares"""

#pedir el valor en pesos chilenos
pesos_chile = int(input("Ingrese la cantidad de dinero a convertir: "))

#valor actual de 1 dolar EU a pesos Chilenos
dolar = 797.33
#conversion y redondeo
conver= round(pesos_chile / dolar , 2)
print(f"Su valor convertido es: ${conver} usd")