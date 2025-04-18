class Cloth:
   # Class attribute
   price = 4000

   @classmethod
   def showPrice(cls):
      return cls.price

# Accessing class attribute
del Cloth.price
print(Cloth.showPrice())  

