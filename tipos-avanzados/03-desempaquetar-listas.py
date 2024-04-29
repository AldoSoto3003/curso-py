""" Desempaquetar listas en variables """

numeros = [1,2,3]

# FEO, MALAS PRACTICAS:
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, *_ = numeros
print(primero,_)
