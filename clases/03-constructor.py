class Perro:
    
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    def habla(self):
        print(f"{self.nombre} dice: Guau!")
        
mi_perro = Perro("Scrappy",10)
mi_perro2 = Perro("Caramelo",12)

mi_perro.habla()
