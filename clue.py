"""importar dependencias para seleccion de colores"""
import termcolor

"""importar algoritmo lógico"""
from logic import *

"""crear clases con nombres o simbolos que representen cada proposición"""
mustard = Symbol("mustard")
plum = Symbol("plum")
scarlet = Symbol("scarlet")
characters = [mustard, plum, scarlet] # lista de personajes

"""escenarios disponibles"""
ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library] # lista de escenarios

"""armas disponibles"""
knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench] # lista de armas

"""crear base de conocimiento"""
symbols = characters + rooms + weapons

"""algoritmo"""

def check_knowledge(knowledge): # la KB trata de sacar conclusiones sobre lo que sé
    for symbol in symbols: # iterar sobre cada símbolo para saber si el símbolo es verdadero o falso
        
        """si el símbolo es verdadero, imprimir en verde"""
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        
        # funciona cuando estamos seguro de que nuestro símbolo no es verdadero
        elif not model_check(knowledge, Not(symbol)): # comprobando si el símbolo no es verdadero
            print(f"{symbol}: MAYBE")

"""crear base de conocimiento"""
# knowledge = And(
#     Or(mustard, plum, scarlet), # cada personaje es mustard, plum o scarlet
#     Or(ballroom, kitchen, library), # cada escenario es ballroom, kitchen o library
#     Or(knife, revolver, wrench), # cada arma es knife, revolver o wrench

#     # a partir de aquí se agregan las proposiciones que se conocen o que se inventan
#     # Add the information from the three initial cards we saw
#     Not(mustard),
#     Not(kitchen),
#     Not(revolver),

#     # Add the guess someone made that it is Scarlet, who used a wrench in the library
#     Or(Not(scarlet), Not(library), Not(wrench)),

#     # Add the cards that we were exposed to
#     Not(plum),
#     Not(ballroom)
# )

knowledge = And(
    Or(mustard, plum, scarlet), # cada personaje es mustard, plum o scarlet
    Or(ballroom, kitchen, library), # cada escenario es ballroom, kitchen o library
    Or(knife, revolver, wrench), # cada arma es knife, revolver o wrench
)
# a partir de aquí se agregan las proposiciones que se conocen o que se inventan
"""knowledge.add -> permite agregar lógica adicional"""
knowledge.add(Not(mustard))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))

knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

knowledge.add(Not(plum))

knowledge.add(Not(ballroom))

"""imprimir resultados"""
check_knowledge(knowledge)