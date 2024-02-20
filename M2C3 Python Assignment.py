cadena ="murcielago ambulante"
guarismo = 7
lista = ["cordero", "gallina", "pavo", "ganso"]
eleccion = True
names = 'harry,alex,susie,jared,gail,conner'

caracteres = cadena[:3]

primero_lista = lista[0]
print(primero_lista)

guarismo_nuevo = guarismo + 10
print(guarismo_nuevo)

ultimo_lista = lista[-1]
print(ultimo_lista)

nueva_lista = names.split(",")
print(nueva_lista)

primero_cadena = cadena.split()[0].upper()
print(primero_cadena)

nueva_cadena = primero_cadena + cadena[10:]
print(nueva_cadena)

final= nueva_cadena + " " + str(guarismo)
print(final)

print("hello world")