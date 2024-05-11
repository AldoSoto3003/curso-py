class Perro:
    
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def __del__(self):
        print("Chao perro")
        
    def __str__(self) -> str:
        return f"clase perro: {self.nombre}"
        
    def habla(self):
        print(f"{self.nombre} dice .")

perro = Perro("Scrappy",7)
del perro