class Employee:
    empCount = 0

    # usamos __init__ para incializar la clase
    def __init__ (self, name, salary): # parámetro self para hacer referencia a sí mismos
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount (self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee (self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)

# creando instancias -> llamando al objeto
emp1 = Employee ("Zara", 2000)
emp2 = Employee ("Manni", 5000)

# acceder al objeto
emp1.displayEmployee()
emp2.displayEmployee()

print ("Total Employee %d" % Employee.empCount)


("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

# __name__
#     Representa el nombre de la clase.
#     En tu código: Employee.__name__ devolverá "Employee".

# __module__
#     Indica el módulo en el que se define la clase.
#     Si la clase está en el mismo script, devolverá "__main__", pero si está en otro archivo, devolverá el nombre del módulo.
#     En tu código: Employee.__module__ indicará dónde se definió la clase.

# __bases__
#     Es una tupla que muestra las clases base (superclases) de la clase.
#     En tu código: Employee.__bases__ devolverá una tupla con las clases padre de Employee.

# __dict__
#     Es un diccionario que contiene los atributos y métodos de la clase.
#     En tu código: Employee.__dict__ devolverá un diccionario con los métodos y variables de clase.

# continuar con -> Built-in Class of Python datatypes