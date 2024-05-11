class Perro:
    patas = 4
    
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    @classmethod
    def habla(cls):
        print("Guau!")
    
    @classmethod
    def factory(cls):
        return cls("chanchito feliz",4)
      
Perro.habla()
perro1 = Perro("Chanchito", 2)
perro2 = Perro("Felipe", 3)
perro3 = Perro.factory()

print(perro3.edad, perro3.nombre)