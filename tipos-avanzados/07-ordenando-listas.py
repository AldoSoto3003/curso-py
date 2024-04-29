numeros = [7,1,45,13,9,123,85]

# Para ordenar elementos ascendientemente
numeros.sort()

# Para ordenar elemntos descendientemente
numeros.sort(reverse=True)

# Para ordenar elementos ascendientemente, PERO nos retorna una nueva lista
numeros2 = sorted(numeros)

# Para ordenar elementos descendientemente, PERO nos retorna una nueva lista
numeros2 = sorted(numeros, reverse=True)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5],        
]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena, reverse=True)

print(usuarios)
