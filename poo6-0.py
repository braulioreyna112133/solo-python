# Dinámicamente agregar un método de clase a una clase

# Clase definida sin métodos inicialmente
class userVision:
    pass

# Definir un método de clase -> recibe la clase como primer argumento (cls)
@classmethod
def userVisionMethod(cls):
    print('The users vision worsened to total blindness')

# Usar la función setattr(objeto, nombre, valor) para agregar el método a la clase
# Nota: al agregar un @classmethod manualmente, debemos usar 'classmethod' explícitamente
setattr(userVision, 'this_is_a_name', classmethod(userVisionMethod))

# Crear un nuevo objeto instanciando la clase
newObj = userVision()

# Llamar al método agregado dinámicamente desde la instancia
newObj.this_is_a_name()
