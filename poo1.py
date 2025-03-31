class pilots ():
    def __init__ (self, pathology, age, avgTimeResponse):
        self.pathology = pathology
        self.age = age
        self.avgTimeResponse = avgTimeResponse

# creando una instancia para llamada a la clase
user = pilots (pathology='full',age=20,avgTimeResponse='fast')
print (user.pathology, user.age, user.avgTimeResponse)
        

