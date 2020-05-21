class Coche:

  #ATRIBUTOS
  marca="Sentra"
  asientos= "6"
  pasajeros="2"
  cinturon="6"
  placas="WUl-f06-35"
  color="Blanco"
  llantas="4"
  velocidad="950 km/h"
  volante="1"
  rines="4"

  #METODOS
  def encender (self):
    print("Encender")
  def apagar (self):
    print("Apagar")
  def frenar (self):
    print("Frenar")
  def manejar (self):
    print("Manejar")
  def frenar(self):
    print("Transportar")

  def __init__(self):
    print("Constructor Coche")

objeto_coche= Coche()
objeto_coche.encender()
objeto_coche.apagar()
objeto_coche.manejar()
objeto_coche.transportar()
objeto_avion.frenar()


print(objeto_coche.marca)
print(objeto_coche.color)
print(objeto_coche.asientos)
print(objeto_coche.pasajeros)
print(objeto_coche.cinturon)
print(objeto_coche.placas)
print(objeto_coche.llantas)
print(objeto_coche.velocidad)
print(objeto_coche.volante)
print(objeto_coche.rines)