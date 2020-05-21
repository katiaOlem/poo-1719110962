class Calculadora:

  #ATRIBUTOS
  numeros="0-9"
  espacios="1"
  puntos="uno . ,dos: ,punto y coma; "
  comas="una , "
  grados="°C"
  comillas="dos"
  fracciones="20/50"
  multiplicaciones="5X4, 8*3 "
  sumas="5+5"
  restas="1-8"

 #METODOS
  def encender (self):
    print("Encender")
  def apagar (self):
   print("Apagar")
  def restar (self):
   print("Restar")
  def mostrar(self):
   print("Mostrar")
  def funcionar(self):
   print("Funcionar")

  def __init__(self):
   print("Constructor Calculadora")

objeto_calculadora= Calculadora ()
print(objeto_calculadora.numeros)
print(objeto_calculadora.espacios)
print(objeto_calculadora.puntos)
print(objeto_calculadora.comas)
print(objeto_calculadora.grados)
print(objeto_calculadora.comillas)
print(objeto_calculadora.fracciones)
print(objeto_calculadora.multiplicaciones)
print(objeto_calculadora.restas)
print(objeto_calculadora.sumas)


