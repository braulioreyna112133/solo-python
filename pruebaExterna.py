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