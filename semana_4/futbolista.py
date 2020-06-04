class Futbolista():

  #ATRIBUTOS
  nombre= "Luis"
  apellidos="Ronaldo"
  edad="23 años"
  numero_seguro="17191109"
  direccion="Residencia #215 Mexico"

 #METODOS
  def correr(self):
   print("Correr")
  def golpear(self):
    print("Golpear")
  def __init__(self):
    print("Constructor Futbolista")

 
class FutbolistaLuis(Futbolista):

 #ATRIBUTOS
  club="America"
  numero="17"
  posicion="Delantero"
  uniforme="Amarillo"
  liga="MX"

 #METODOS
  def correr(self):
   print("Correr mas de 10 km")
  def golpear(self):
   print("Golpear el balon para meter gol")
  def quitar(self):
   print("Quitar")
  def golear(self):
    print("Golear")
  def __init__(self):
   print("Constructor Futbolista Luis")


objeto_futbolista= FutbolistaLuis()
objeto_futbolista.correr()
objeto_futbolista.golpear()
objeto_futbolista.quitar()
objeto_futbolista.golear()
objeto_futbolista.nombre="Luis Fernando "
print(objeto_futbolista.nombre)
objeto_futbolista.apellidos="Ronaldo Aguirre"
print(objeto_futbolista.apellidos)
objeto_futbolista.edad="25 años Actualmente"
print(objeto_futbolista.edad)
objeto_futbolista.numero_seguro="17191109 del Imss"
print(objeto_futbolista.numero_seguro)
objeto_futbolista.direccion="calle Residencia #215 col. Zafiro Mexico"
print(objeto_futbolista.direccion)
print(objeto_futbolista.club)
print(objeto_futbolista.numero)
print(objeto_futbolista.posicion)
print(objeto_futbolista.uniforme)
print(objeto_futbolista.liga)