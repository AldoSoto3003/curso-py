class Perro:
    patas = 4
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def habla(self):
        print(f"{self.nombre} dice: Guau!")
      
mi_perro = Perro("Scrappy", 1)
mi_perro.patas = 5

print(Perro.patas)
print(mi_perro.patas)
