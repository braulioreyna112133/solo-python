# Revisar para hoy:
# Dynamically Add Class Method to a Class
# Dynamically Delete Class Methods

'''Dynamically Add Class Method to a Class'''

# clase definida por defecto o no mutable
class userVision:
    pass

# iniciar classmethod -> permite el acceso a los atributos 
# de la clase para poder agregar métodos
@classmethod
def userVisionMethod (cls):
    print ('the users vision worsened to total blindness')

# uso de la función setattr() function
# setattr (object, name, value)
setattr (userVision, 'this_is_a_name', userVisionMethod)
newObj = userVision ()
newObj.this_is_a_name()