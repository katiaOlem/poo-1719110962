class Avion:

  #ATRIBUTOS
  nombre="Polaris"
  asientos= "400"
  pasajeros="300"
  vuelo="344"
  direccion="Los Ángeles"
  color="Blanco"
  tamaño="Mediano"
  velocidad="950 km/h"
  altura= " 10 km "
  control="Automatico"

  #METODOS
  def encender (self):
    print("Encender")
  def apagar (self):
    print("Apagar")
  def aterrizar (self):
    print("Aterrizar")
  def volar (self):
    print("Volar")
  def frenar(self):
    print("Frenar")
  def __init__(self):
    print("Constructor Avion")

objeto_avion= Avion()
objeto_avion.encender()
objeto_avion.apagar()
objeto_avion.aterrizar()
objeto_avion.volar()
objeto_avion.frenar()


print(objeto_avion.nombre)
print(objeto_avion.asientos)
print(objeto_avion.pasajeros)
print(objeto_avion.vuelo)
print(objeto_avion.direccion)
print(objeto_avion.color)
print(objeto_avion.tamaño)
print(objeto_avion.velocidad)
print(objeto_avion.altura)
print(objeto_avion.control)