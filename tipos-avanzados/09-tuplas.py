
numeros = (1,2,3,4,5,6,7,8,9,10)
print(numeros)

punto = tuple([1,2])
print(punto)

# Desempaquetado de tupla:
primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

# Esto da ERROR, porque las TUPLAS NO se pueden modificar
numeros[0] = 10