
# Ejemplo 2: usando decorador classmethod, forma 1

# classmethod(instance_method)
# Usa un método de instancia cuando necesitas 
# trabajar con datos específicos de un objeto.

# Usa un método de clase cuando necesitas modificar 
# algo a nivel de clase o crear objetos de forma especial.

class objects:
    human = 'human'

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def show (self):
        print (f'Type: {self.human}: {self.name}, {self.age}')

    @classmethod
    def addPatholgy (cls, pathology):
        cls.human = pathology

# llamada de clase
user = objects ('Braulio', 21)
user.show()

# Braulio presenta un problema
objects.addPatholgy ('blind human')
user.show()
print(objects.human)