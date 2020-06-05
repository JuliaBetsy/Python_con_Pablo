# discoteca untsunts

import random
from string import Template

MAX_HIGADO = 100


class Persona:
    def __init__ (self, nombre = "el señor tofu", aforo=100):
        self.nombre = nombre
        self.aforoMaximo = aforo
        self.dinero = 0
        self.colaEntrada = []
        self.genteDentro =[]

    def añadirColaEntrar (self, persona):

        self.ColaEntrada.append (persona)

    def intentarPasar (self):

        if (len (self.genteDentro) < aforoMaximo):

            siguiente = self.colaEntrada.pop (0)
            if (siguiente.calcetines != "blancos"):
                self.genteDentro.append (siguiente)
            else:
                print ("heute leider nicht " + siguiente.nombre)
        else:
            print ("no hay mas hueco")
           



        
      
                   




   


