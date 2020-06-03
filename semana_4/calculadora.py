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
  def encender (self):
    print("Encender con el boton ON ") #POLIMORFISMO
  def apagar(self):
    print("Apagar un con el boton OFF")
  def restar (self):
    print("Restar")
  def borrar (self):
    print("Borrar")
  def __init__(self):
    print("Constructor Calculadora Cientifica")
  

objeto_calculadora= CalculadoraCientifica ()
objeto_calculadora.encender()
objeto_calculadora.apagar()
objeto_calculadora.restar()
objeto_calculadora.borrar()
objeto_calculadora.tipo="Calculadora Cientifica" #POLIMORFISMO
print(objeto_calculadora.tipo)
objeto_calculadora.numero="numeros del 0 al 9"
print(objeto_calculadora.numeros)
objeto_calculadora.espacios="Espacio para separar las Funciones"
print(objeto_calculadora.espacios)
objeto_calculadora.puntos="Punto y coma, puto decimal"
print(objeto_calculadora.puntos)
objeto_calculadora.comas="Tiene coma para separar las cantidades decimales,millones etc."
print(objeto_calculadora.comas)
print(objeto_calculadora.grados)
print(objeto_calculadora.funcion)
print(objeto_calculadora.pantalla)
print(objeto_calculadora.ecuaciones)
print(objeto_calculadora.boton)
