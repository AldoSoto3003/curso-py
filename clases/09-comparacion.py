class Coordenadas():
    
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon
    
    def __eq__(self, value: object) -> bool:
        return self.lat == value.lat and self.lon == value.lon 
    
    def __ne__(self, value: object) -> bool:
        return self.lat != value.lat or self.lon != value.lon 
    
    def __lt__(self,value:object) -> bool:
        return self.lat + self.lon < value.lat + value.lon

    def __le__(self,value: object) -> bool:
        return self.lat + self.lon <= value.lat + value.lon
        

coords1 = Coordenadas(45,27)
coords2 = Coordenadas(45,27)

print(coords1 <= coords2)
