class celular ():
    marca = 'apple'
    modelo = '16'
    camara = '48 mpx'

objetoCelular = celular ()
print (objetoCelular.marca)
    

class Celular2 ():
    def __init__ (self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
objetoCelular2 = Celular2 ('apple', '16', '48mpx')
print (objetoCelular2.modelo)