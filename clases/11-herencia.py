class Animal:
    def comer(self):
        print("comiendo")
    
class Perro(Animal):
    def pasear(self):
        print("paseando")
            
class Chanchito(Animal):
    def programar(self):
        print("programando")
        
perro = Perro()
perro.comer()