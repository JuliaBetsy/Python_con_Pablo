# persona

import random
from string import Template

class Persona:
    def __init__ (self, nombre):
        self.nombre = nombre

        self.calcetines = random.choice(["blancos", "magenta", "furcia"])

    def presentate (self):
                
        presentacion=Template("Holi me llamo $nombre y tengo calcetines $color ")
        print (
            presentacion.substitute(
                nombre= self.nombre,
                color= self.calcetines 
            )

        )

