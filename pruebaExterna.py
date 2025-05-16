class RequestsByHardware ():
    def __init__ (self, whatamIseeingAttr, pilotName, adress, responseCalibrator):

        # metodos de que estoy viendo?
        self.pilotName = pilotName
        self.whatamIseeingAttr = whatamIseeingAttr

        # metodos de retorno a casa
        self.adress = adress

        # tipo de comprehensión por dictado
        self.responseCalibrator = responseCalibrator


    def whatamIseeing (self):
        '''simulacion'''
        '''modulo de descripción visual se inicia'''
        print (f'{self.pilotName} estás viendo {self.whatamIseeingAttr}')

    def returnHome (self):
        '''simulacion'''
        '''modulo activado por solicitud, incluye dirección establecida y velocidad de comprehensión'''
        print (f'Estás usando el {self.responseCalibrator}')
        print (f'{self.pilotName} estás en camino a la dirección establecida en {self.adress}')


    
solicitud1 = RequestsByHardware ('urbanismo', 'braulio', 'distrito 11', 'tipo de dictado A')
solicitud1.whatamIseeing()
solicitud1.returnHome()