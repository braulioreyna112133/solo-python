# uso del decorador classmethods()

# classmethod(instance_method)
# Usa un método de instancia cuando necesitas trabajar con datos específicos de un objeto.

# Usa un método de clase cuando necesitas modificar algo a nivel de clase o crear objetos de forma especial.


# Ejemplo 1: utilizando método de instancia
class pilotIdentification:
    def __init__ (self, pathology, age, soundLevel):
        self.pathology = pathology
        self.age = age
        self.soundLevel = soundLevel

    def outputConfig (self):
        print (f'Info user config: {self.pathology}, {self.age}, {self.soundLevel}')

userConfig = pilotIdentification ('full blind user', 5, 'higha adaptable')
userConfig.outputConfig()
