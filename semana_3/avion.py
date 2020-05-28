class Avion:

  #ATRIBUTOS
  nombre="Polaris"
  asientos= "400"
  pasajeros="300"
  vuelo="344"
  direccion="Los Ángeles"
  #METODOS
  def controlar(self):
    print("Controlar")
  def encender(self):
    print("Encender")
  def __init__(self):
    print("Constructor Avion")

class AvionPolaris():
  #ATRIBUTOS
  llantas="4"
  volante="Estandar"
  control="Manual"
  alas="2"
  motor="Turbina de gas"
  #METODOS
  def volar(self):
    print("Volar")
  def aterrizar(self):
    print("Aterrizar")
  def __init__(self):
    print("Constructor Avion Polaris")

objeto= Avion()
objeto.controlar()
objeto.encender()
print(objeto.nombre)
print(objeto.asientos)
print(objeto.pasajeros)
print(objeto.vuelo)
print(objeto.direccion)

objeto_polaris= AvionPolaris()
objeto_polaris.controlar()
objeto_polaris.encender()
objeto_polaris.volar()
objeto_polaris.aterrizar()
print(objeto_polaris.nombre)
print(objeto_polaris.asientos)
print(objeto_polaris.pasajeros)
print(objeto_polaris.vuelo)
print(objeto_polaris.direccion)
print(objeto_polaris.llantas)
print(objeto_polaris.volante)
print(objeto_polaris.control)
print(objeto_polaris.alas)
print(objeto_polaris.motor)