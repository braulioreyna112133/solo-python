# Uso de métodos de instancia. 
# Son los métodos "tradiconales" son aquellos que hacen referencia a sí mismos


# 1 crear una clase
class pilotTest:
    pilot = 'Piloto de prueba'

    # 2 definir función
    # 3 incialicializar función con un __init__
    # 4 referenciar la función a sí misma -> métodos de instancia
    def __init__ (self, request):
        
        # 5 definir variable de instancia
        self.request = request

    def looking (self):
        print(f"{self.request} es un escenario observable")

    def info (self):
        print(f"{self.request} es observada por un {self.pilot}")

firulais = pilotTest("Area X")
firulais.looking()  
firulais.info()    
