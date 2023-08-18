#recorrer string y lista

def main():
    palabra = str(input("Ingrese nombre: "))
    for letra in palabra:
        print (letra)
    lista=["el1","el 2","el3","el 4","el 5"]
    for elemento in lista:
        print(elemento)
        
    for elemento in lista[0:2]:  #mostrar una parte de una lista
        print(elemento)
    
    for elemento in lista[::-1]:  #mostrar al reves
        print(elemento)
        
        
if(__name__=="__main__"):
    main()