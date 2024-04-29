
usuarios = [
    ["Chanchito",4],
    ["Felipe",1],
    ["Pulga",5],
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# MAP
nombres = [usuario[0] for usuario in usuarios]

# FILTER
nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# MAP WITH FUNCTION
nombres = list(filter(lambda usuario:usuario[0], usuarios))
print(nombres)

# FILTER WITH FUNCTION
nombres = list(filter(lambda usuario:usuario[1] > 2, usuarios))
print(nombres)