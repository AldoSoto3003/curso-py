""" Operador de desempaquetamiento """

# DESEMPAQUETADO DE LISTAS
lista1 = [10,20,30,40]

def n(n1,n2,n3,n4):
    print(f"N1:{n1} N2:{n2} N3:{n3} N4:{n4} ")

n(*lista1)

lista2 = [5,6]
combinada = ["Hola ", *lista1, "Mundo ", *lista2]

print(combinada)

# DESEMPAQUETADO DE DICCIONARIOS
punto1 = {"x":20}
punto2 = {"y":15}

nuevo_punto = {**punto1, "lala":"Hola mundo", **punto2, "z": "mundo"}
print(nuevo_punto)