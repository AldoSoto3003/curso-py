""" 
    set es una coleccion de datos que NO se pueden repetir y NO estan ordenados 
    y tampoco podemos acceder a uno de ellos como: set[0]
"""

primer_set = {1, 1, 2, 2, 3, 4,}
lista = [3, 4, 5]
segundo_set = set(lista)

#UNION
#(todos los datos)
print(primer_set | segundo_set)

#INTERSECCION
#(los datos que estan en ambos)
print(primer_set & segundo_set )

#DIFERENCIA 
#(los datos que solo se encuentran en el primer set y eliminar los que esten tambien en el segundo set)
print(primer_set - segundo_set)

print(primer_set ^ segundo_set)