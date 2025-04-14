# podemos declar el valor de una variable desde adentro de la clase
# cuando queremos que el valor de la variable sea fijo

class cloth:
    def __init__ (self):
        self.price2 = 4000
    
    def showPrice (self):
        return self.price2

cloth_class = cloth ()
print (cloth_class.showPrice())
   

# si el valor de la variable será distinto podemos setearlo desde afuera
# con los parámetros

class Cloth2:
    def __init__ (self, price2): # inicalizamos la clase con el constructor y el parámetro price
        self.price2 = price2

    def showPrice2 (self):
        return self.price2
    
# creamos el objeto
price2_class = Cloth2('$ 1,200')

# llamamos al método del objeto
print (price2_class.showPrice2())