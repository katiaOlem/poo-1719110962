class Calculadora():
  #ATRIBUTOS
  tipo="Cientifica"
  numeros="0-9"
  espacios="1"
  puntos="uno . ,dos: ,punto y coma; "
  comas="una , "
  #Metodos
  def encender(self):
    print("Encender")
  def apagar(self):
    print("Apagar")
  def __init__(self):
    print("Constructor Calculadora")
  
class CalculadoraCientifica(Calculadora):
  #ATRIBUTOS
  grados="°c"
  funcion="Seno, coseno, etc."
  pantalla="alta Resolucion"
  ecuaciones="Calculo"
  boton="Cancelar"

  #METODOS
  def restar (self):
    print("Restar")
  def borrar (self):
    print("Borrar")
  def __init__(self):
    print("Constructor Calculadora Cientifica")
  
objeto= Calculadora ()
objeto.encender()
objeto.apagar()
print(objeto.tipo)
print(objeto.numeros)
print(objeto.espacios)
print(objeto.puntos)
print(objeto.comas)

objeto_calculadora= CalculadoraCientifica ()
objeto_calculadora.encender()
objeto_calculadora.apagar()
objeto_calculadora.restar()
objeto_calculadora.borrar()
print(objeto_calculadora.tipo)
print(objeto_calculadora.numeros)
print(objeto_calculadora.espacios)
print(objeto_calculadora.puntos)
print(objeto_calculadora.comas)
print(objeto_calculadora.grados)
print(objeto_calculadora.funcion)
print(objeto_calculadora.pantalla)
print(objeto_calculadora.ecuaciones)
print(objeto_calculadora.boton)
