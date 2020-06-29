# discoteca untsunts

import random
from string import Template

MAX_HIGADO = 100


class Discoteca:
    def __init__ (self, nombre = "el señor tofu", aforoMaximo=100):
        self.nombre = nombre
        self.aforoMaximo = aforoMaximo
        self.dinero = 0
        self.colaEntrada = []
        self.genteDentro =[]

    def añadirColaEntrar (self, persona):

        self.colaEntrada.append (persona)

    def intentarPasar (self):

        if (len (self.genteDentro) < self.aforoMaximo):

            siguiente = self.colaEntrada.pop (0)
            if (siguiente.calcetines != "blancos"):
                self.genteDentro.append (siguiente)
            else:
                print ("heute leider nicht " + siguiente.nombre)
        else:
            print ("no hay mas hueco")
           



        
      
                   




   


