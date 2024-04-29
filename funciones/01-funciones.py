""" 01 funciones"""

def hola(nombre, apellido = 'Feliz'):
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}")
    
    
#Argumentos convencionales
hola("Aldo","Soto")

#Argumento opcional (Apellido)
hola("Chanchito")

#Argumentos nombrados
hola(apellido="Soto", nombre="Aldo")