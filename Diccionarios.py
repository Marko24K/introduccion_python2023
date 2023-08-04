#son una coleccion que se utiliza para almacenar valores que tienen una relacion entre si
# se definen con {} y se separan con ,
#no tienen indices numericos
diccionario={
    "nombre": "Luigi",
    "apellido":"Bross",
    "Apodo":"Mario verde",
    "edad" : 25,
    "es_verde": True,
    "estatura" : 1.5
}
print(diccionario["nombre"])
print(len(diccionario)) #cantidad de elementos en un diccionario

#metodo para obtener el valor de un elemento
print(diccionario.get("es_verde"))

#metodo para eliminar un elemento
diccionario.pop("Apodo")
print(diccionario)

#modificar un elemento 
diccionario["nombre"] = "Mario"
diccionario.update({"apellido":"Castañeda"})
print(diccionario)

#obtener lista de llaves/claves/indices
print(diccionario.keys())

#obtener lista de valores
print(diccionario.values())