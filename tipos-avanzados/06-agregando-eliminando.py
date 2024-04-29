
MASCOTAS = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito feliz"
]

#para insertar en un indice en especifico y reordenar el resto
MASCOTAS.insert(1,"Melvin")
#para insertar al final de la lista
MASCOTAS.append("Chanchito triste")

#para eliminar un elemnto de la lista, OJO: elimina al primer elementro que encuentre coincidencia
MASCOTAS.remove("Pulga")
#para eliminar el ultimo elemento de la lista
MASCOTAS.pop()
#para eliminar el elemento que le corresponda al indice
MASCOTAS.pop(1)
#para eliminar el elemento que le corresponda al indice
del MASCOTAS[0]
#para limpiar TODA la lista
MASCOTAS.clear()

print(MASCOTAS)
