import json
from pathlib import Path

# Crear y escribir en un archivo JSON
# productos = [
#     {"id":1, "name":"Surfboard"},
#     {"id":2, "name":"Bicicleta"},
#     {"id":3, "name":"Skate"},
# ]

# data = json.dumps(productos)
# Path("../archivos/productos.json").write_text(data=data)

# Leer de un JSON
data = Path("../archivos/productos.json").read_text(encoding='utf-8')
productos = json.loads(data)

# Modificar JSON
productos[0]["name"] = "Chanchito feliz"
Path("../archivos/productos.json").write_text(json.dumps(productos))