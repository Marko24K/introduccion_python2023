#palindromo
#palabra que se lee igual al derecho y al reves
#ana
#luz azul
# Otto

#escribir una funcion que identifique si una palabra es palindromo o no
def palindromo(palabra):
    palabra = palabra.strip() #eliminar espacios vacios despues de la oracion
    palabra = palabra.lower() #converti todo a minusculas
    palabra = palabra.replace(" ", "") #reemplazar espacios en la palabra 
    invertida = palabra[::-1]
    if palabra == invertida:
        return True
    else:
        return False


""" 
palabra = input("ingrese palabra: ")
resultado = palindromo(palabra)
if resultado:             
    print("es palindromo")
else:
    print("no es palindromo") 

"""
def main():
     #pass #algo momentaneo para que la funcion no este vacia

    palabra = input("ingrese palabra: ")
    resultado = palindromo(palabra)
    if resultado:             
       print("es palindromo")
    else:
        print("no es palindromo") 

if __name__ == '__main__': #punto de entrada
    main()