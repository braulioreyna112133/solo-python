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
        self.request = request # es como una variable vacía

    def looking (self):
        print(f"{self.request} es un escenario observable")

    def info (self):
        print(f"{self.request} es observada por un {self.pilot}")

user = pilotTest("Area X")
user.looking()  
user.info()    


# Se llama a la clase y se pasa "Area X" como argumento posicional al método __init__,
# el cual inicializa la variable de instancia `self.request` con ese valor.

# La variable de instancia `self.request` no está vacía. Se inicializa con el valor
# proporcionado al crear la instancia (en este caso, "Area X"). Si no se proporciona
# un argumento al instanciar la clase, se generará un error porque el argumento es obligatorio.