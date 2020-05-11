import persona

lista=[]
nombres = ["Juan", "Pepe", "Dieter"] 

for nombre in nombres:
    print (nombre)

    lista.append (persona.Persona (nombre))

pass

for p in lista:
    p.presentate ()

pass

    