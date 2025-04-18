'''Dynamically Delete Class Methods
The Python del operator is used to delete a class method dynamically. 
If you try to access the deleted method, the code will raise AttributeError'''

class userUsers:
    def __init__ (self):
        pass

    @classmethod
    def pilotName (cls):
        print ('Pilot name: Raymond')

del userUsers.pilotName

def checkerClassWorking():
    try:
        userUsers.pilotName()
    except AttributeError:
        print (AttributeError)

checkerClassWorking()



