class Pilots:
    def __init__ (self, ID, pathology):
        self.__ID = ID
        self.__pathology = pathology
        print ('ID', self.__ID, 'Pathology', self.__pathology)

pilot1 = Pilots (234, 'Full')
pilot2 = Pilots (777, 'Full')
