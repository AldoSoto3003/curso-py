""" Diccionarios """

punto = {"x": 25,"y":30}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

if "lala" in punto:
    print(punto, punto["lala"])

print(f"El punto X con GET: {punto.get("x")}")
print(f"El punto lala con GET: {punto.get("lala", 1)}")

del punto["x"]
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])
    
for llave,valor in punto.items():
    print(llave, valor)
    
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])