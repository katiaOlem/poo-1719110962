class Futbolista:

#ATRIBUTOS

 nombre="Ismael"
 nacionalidad="Mexicana"
 equipo="Pachuca"
 jugador="11"
 numero= "05"
 color="Azul"
 liga="MX"
 posicion="Delantero"
 faltas="25"
 goles="15"

#METODOS

 def correr (self):
    print("Correr")
 def golpear(self):
    print("Golpear")
 def jugar (self):
    print("Jugar")
 def avanzar(self):
    print ("Avanzar")
 def golear(self):
    print("Golear")
  
 def __init__(self):
    print("Constructor Futbolista")

objeto_futbolista= Futbolista()
objeto_futbolista.correr()
objeto_futbolista.golpear()
objeto_futbolista.jugar()
objeto_futbolista.avanzar()
objeto_futbolista.golear()

print(objeto_futbolista.nombre)
print(objeto_futbolista.nacionalidad)
print(objeto_futbolista.equipo)
print(objeto_futbolista.jugador)
print(objeto_futbolista.numero)
print(objeto_futbolista.color)
print(objeto_futbolista.liga)
print(objeto_futbolista.posicion)
print(objeto_futbolista.faltas)
print(objeto_futbolista.goles)