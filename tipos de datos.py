#tipos de datos
# en python todo es un objeto

# 1) numeros enteros (int integer) 5 8 9 878 7

# 2) N. DECIMALES (float flotantes) 4.5 6.8 5.6666676 7.0  
decimal = 23.6
# 3) cadenas de texto (string str) 
frase="hola niños"
frase2='hola sjdjsdj'
frase3=""" "fsdfsdfgdf " 'sdfdfsfs d' nfjmngfjnfgmklnfgmnfgm""" 
print(frase3)
print(frase + " " + frase2)
#4) booleanos (true false)
estudiante=True
trabaja=False

print(estudiante)
print (trabaja)
#Convertir tipos de datos

numero1=input ("ingrese un numero: ")
numero2=input("ingrese otro numero: ")

print(numero1 + numero2) #se concatenan


print(int(numero1)+int(numero2))

decimal2= 125.77
print(int(decimal2))

n=23
print(float(n))

print("el numero es: " + str(n))