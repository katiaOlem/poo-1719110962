class Vacaciones():
  #ATRIBUTOS
  lugar= "Cancun"
  dia="23"
  ano="2020"
  personas="2"
  transporte=("Autobus")

#METODOS
  def transportar(self):
    print("Transportar")
  def relajar(self):
    print("Relajar")
  def __init__(self):
    print("Constructor Vacaciones")


class VacacionesCancun (Vacaciones):

  #ATRIBUTOS
  voletos="2"
  hotel="5 estrellas"
  recamara="Suite"
  tiempo="Tres semanas"
  paquete="7 Estrellas"

  def divertir(self):
    print("Divertir")
  def disfrutar(self):
    print("Disfrutar")
  def __init__(self):
    print("Constructor Vaciones Cancun")
  
objeto= Vacaciones()
objeto.transportar()
objeto.relajar()
print(objeto.lugar)
print(objeto.dia)
print(objeto.ano)
print(objeto.personas)
print(objeto.transporte)

objeto_vacaciones_cancun= VacacionesCancun()
objeto_vacaciones_cancun.transportar()
objeto_vacaciones_cancun.relajar()
objeto_vacaciones_cancun.divertir()
objeto_vacaciones_cancun.disfrutar()
print(objeto_vacaciones_cancun.lugar)
print(objeto_vacaciones_cancun.dia)
print(objeto_vacaciones_cancun.ano)
print(objeto_vacaciones_cancun.personas)
print(objeto_vacaciones_cancun.transporte)
print(objeto_vacaciones_cancun.voletos)
print(objeto_vacaciones_cancun.hotel)
print(objeto_vacaciones_cancun.recamara)
print(objeto_vacaciones_cancun.tiempo)
print(objeto_vacaciones_cancun.paquete)