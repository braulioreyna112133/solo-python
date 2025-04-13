# uso del decorador classmethods()

# Ejemplo 1: utilizando método de instancia
class pilotIdentification:
    def __init__ (self, pathology, age, soundLevel):
        self.pathology = pathology
        self.age = age
        self.soundLevel = soundLevel

    def outputConfig (self):
        print (f'Info user config: {self.pathology}, {self.age}, {self.soundLevel}')

userConfig = pilotIdentification ('full blind user', 5, 'high-adaptable')
userConfig.outputConfig()

