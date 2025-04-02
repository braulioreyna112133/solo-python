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

# continuar con -> Built-in Class of Python datatypes