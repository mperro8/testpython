



# nombres = ["Juan", "Pedro", "Maria", "Ana", "luis"]

# # print (type(nombres))
# # print (nombres [0])

# # Cambio el primer nombre a "Pablo":
# nombres[1] = "Pablo"

# print (nombres)

# # La funcion len() nos devuelve la longitud
# print (len(nombres))

# # metodo append para agregar elemento al final de la lista
# nombres.append ("Cacho")

# print (nombres)

# print (len(nombres))

# # metodo insert para "insertar" un elemento en el puesto indicado
# nombres.insert (2, 455210)

# print (nombres)

# print (len(nombres))

# # formas de recorrer una lista:

# for nombre in nombres:
#     print (nombre)


#---------------------------------------

# nombre = "Juan"
# nombre_dos = "Federico"
# print (nombre)
# print (nombre_dos)

# # Asignación multiple:

# # nombre, nombre_dos = "Florencia", "Pedro"

# # O tambien:
# nombre, nombre_dos = "Florencia", input ("Nombre?")

# print (nombre)
# print (nombre_dos)


#-----------------------------------------------

# def sumar_lista (lista_nro):
#     sub_total = 0
#     # Recorrer la lista
#     for nro in lista_nro:
#         sub_total += nro
#     return sub_total

# lista_nros = [2,3,5]

# print (sumar_lista (lista_nros))


# #-----------------------------------

# def generar_lista (cantidad_elementos):
#     lista =[]
#     for i in range (cantidad_elementos):
#         lista.append(i)
#     return lista
# print (generar_lista(20))

# exit ()


#-------------------------------------------

# Metodo para ordenar la lista

# autos = [1,3,6,75,77,344,65,]

# print (autos)

# print ("Ordenando:")

# Metodo sort ordena (reverse = True) lo ordena al reves
# autos.sort(reverse = True)


# Así la imprimo ordenada, tambien puedo usar (reverse = True):
# print (sorted(autos, reverse = True))

# print (autos)
# # imrpimir minimo o maximo de la lista:
# print (max(autos))

# #Imprimir la suma de la lista:

# print (sum(autos))

# # imrpimir rangos o posicion especifica:
# print (autos[0:4])
# print (autos[-1])

#---------------------------------------------
# TUPLAS:

# tupla = (1,2,3,4,5,6,7,8,9,10, 4, 4)

# # Contar un valor dentro de la tupla:

# print (tupla.count(4))

# # Imprimir un valor especifico:

# print (tupla[3])

# print (tupla[2:5])

# -----------------------------------------

# DICCIONARIOS:

dict_1 = {
    "Nombre" : "Juan",
    "Apellido" : "Perez",
    "Edad" : 30,
}

dict_2 = {
    "Nombre" : "Ana",
    "Apellido" : "Gomez",
    "Edad" : 25,
}


print (dict_1["Nombre"])

print (dict_2["Edad"])

# Metodo muestra las claves del diccionario:

print (dict_1.keys())

for i in dict_1.keys():
    print(i)

for i in dict_1.values():
    print(i)

# Muestra clave : valor:
print (dict_2.items())

for clave,valor in dict_2.items():
    print (clave, ": ", valor)
    print ("Clave: ", clave)
    print ("valor: ", valor)

exit()