class Avion():
  #ATRIBUTOS
  nombre="POLARIS"
  asientos="35"
  alas="2"
  llantas="4"
  ventanas="36"

  #Metodos
  def despegar(self):
    print("Despegar")
  def aterrizar(self):
    print("Aterrizar")
  def __init__(self):
    print("Constructor Avion")
  
  #HERENCIA
class AvionPolaris(Avion):
  #ATRIBUTOS
  color="Blanco"
  tamaño="Mediano"
  velocidad="950 km/h"
  altura= " 10 km "
  control="Automatico"

  #Metodos
  def volar(self):
    print("volar")
  def manejar(self):
    print("Manejar")
  def __init__(self):
    print("Constructor Avion Polaris")

objeto=Avion()
objeto.despegar()
objeto.aterrizar()
print(objeto.nombre)
print(objeto.asientos)
print(objeto.alas)
print(objeto.llantas)
print(objeto.ventanas)

objeto_polaris=AvionPolaris()
objeto_polaris.despegar()
objeto_polaris.aterrizar()
objeto_polaris.volar()
objeto_polaris.manejar()
print(objeto_polaris.nombre)
print(objeto_polaris.asientos)
print(objeto_polaris.llantas)
print(objeto_polaris.ventanas)
print(objeto_polaris.color)
print(objeto_polaris.tamaño)
print(objeto_polaris.velocidad)
print(objeto_polaris.altura)
print(objeto_polaris.control)