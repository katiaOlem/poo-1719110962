class Avion():
  #ATRIBUTOS
  nombre="POLARIS"
  asientos="35"
  alas="2 perfil Alar"
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
  color="Blanco con franjas Rojas"
  tamano="Mediano"
  velocidad="950 km/h de velocidad "
  altura= " 10 km de altura "
  control="Automatico"

  #Metodos
  def despegar(self):
    print("Despegar de Cancun")
  def aterrizar(self):
    print("Aterrizar en Mexico")
  def volar(self):
    print("volar")
  def manejar(self):
    print("Manejar")
  def __init__(self):
    print("Constructor Avion Polaris")


objeto_polaris=AvionPolaris()
objeto_polaris.despegar()
objeto_polaris.aterrizar()
objeto_polaris.volar()
objeto_polaris.manejar()
objeto_polaris.nombre= " Boeing 757-200 "
print(objeto_polaris.nombre)
objeto_polaris.asientos= "Asientos de Clase empresarial 25-  United Economy 108 - Plus United Economy 45 "
print(objeto_polaris.asientos)
objeto_polaris.llantas="3 llantas de doble Rodada"
print(objeto_polaris.llantas)
objeto_polaris.alas="1 ala volante"
print(objeto_polaris.alas)
objeto_polaris.ventanas="100 ventanas de resina acrílica y sintética muy resistentes "
print(objeto_polaris.ventanas)
print(objeto_polaris.color)
print(objeto_polaris.tamano)
print(objeto_polaris.velocidad)
print(objeto_polaris.altura)
print(objeto_polaris.control)