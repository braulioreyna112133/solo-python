# hacer ejercicio usando métodos pero ahora definiendo 
# los atributos desde afuera de la clase

class hardwareManualControl:
    def __init__ (self, goTo, what_looking, avgResponse):
        self.goTo = goTo
        self.what_looking = what_looking
        self.avgResponse = avgResponse

'''se puede setear la entrada del objeto mediante los argumentos del objeto'''
goTo =  input ('¿Qué dirección es?: ')
what_looking = input ('¿Qué estoy viendo?: ')
avgResponse = input ('Cambiar velocidad de dictado: ')

# objeto
hardwareControl = hardwareManualControl (goTo, what_looking, avgResponse)
print (hardwareControl.goTo)
