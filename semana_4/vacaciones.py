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

  def transportar (self):
    print("Transportar de su Casa al Aeropuerto Internacional de la Ciudad de México")
  def relajar(self):
    print("Relajar en un Spa de Cancun ")
  def divertir(self):
    print("Divertir")
  def disfrutar(self):
    print("Disfrutar")
  def __init__(self):
    print("Constructor Vaciones Cancun")

objeto_vacaciones_cancun= VacacionesCancun()
objeto_vacaciones_cancun.transportar()
objeto_vacaciones_cancun.relajar()
objeto_vacaciones_cancun.divertir()
objeto_vacaciones_cancun.disfrutar()
objeto_vacaciones_cancun.lugar="Cancun Quintana Roo"
print(objeto_vacaciones_cancun.lugar)
objeto_vacaciones_cancun.dia="23 de Julio"
print(objeto_vacaciones_cancun.dia)
objeto_vacaciones_cancun.ano=" 2020 "
print(objeto_vacaciones_cancun.ano)
objeto_vacaciones_cancun.personas="Cuatro 2 ADULTOS 2 MENORES DE EDAD"
print(objeto_vacaciones_cancun.personas)
objeto_vacaciones_cancun.transporte="Auto y Avion"
print(objeto_vacaciones_cancun.transporte)
print(objeto_vacaciones_cancun.voletos)
print(objeto_vacaciones_cancun.hotel)
print(objeto_vacaciones_cancun.recamara)
print(objeto_vacaciones_cancun.tiempo)
print(objeto_vacaciones_cancun.paquete)