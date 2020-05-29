class Futbolista():

  #ATRIBUTOS
  nombre= "Luis"
  apellido="Ronaldo"
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
  def quitar(self):
   print("Quitar")
  def golear(self):
    print("Golear")
  def __init__(self):
   print("Constructor Futbolista Luis")

objeto= Futbolista()
objeto.correr()
objeto.golpear()
print(objeto.nombre)
print(objeto.apellido)
print(objeto.edad)
print(objeto.numero_seguro)
print(objeto.direccion)

objeto_futbolista= FutbolistaLuis()
objeto_futbolista.correr()
objeto_futbolista.golpear()
objeto_futbolista.quitar()
objeto_futbolista.golear()
print(objeto_futbolista.nombre)
print(objeto_futbolista.apellido)
print(objeto_futbolista.edad)
print(objeto_futbolista.numero_seguro)
print(objeto_futbolista.direccion)
print(objeto_futbolista.club)
print(objeto_futbolista.numero)
print(objeto_futbolista.posicion)
print(objeto_futbolista.uniforme)
print(objeto_futbolista.liga)