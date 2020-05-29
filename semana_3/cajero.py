class Cajero():
  #ATRIBUTOS
  nombre="Full"
  depositos="10.000 - 6,000,000.00"
  retiros="10.000 - 6,000,000.00"
  numeros="0-9"
  pantalla="32 pulgadas"

  #METODOS
  def retirar (self):
    print("Retirar")
  def extraer(self):
    print("Extraer")
  def __init__(self):
    print("Constructor Cajero Automatico")

  #HERENCIA 
  
class CajeroFull(Cajero):
  #ATRIBUTOS
  contraseña="18965"
  chip="si"
  impresora="Matricial"
  tarjetas="Debito, Credito"
  envios="Toda la Republica"

  #METODOS
  def abonar(self):
   print("Abonar")
  def recargar(self):
   print("Recargar")
  def __init__(self):
    print("Constructor Cajero Automatico Full")

objeto= Cajero ()
objeto.retirar()
objeto.extraer()
print(objeto.nombre)
print(objeto.depositos)
print(objeto.retiros)
print(objeto.numeros)
print(objeto.pantalla)

objeto_full=CajeroFull()
objeto_full.retirar()
objeto_full.extraer()
objeto_full.abonar()
objeto_full.recargar()
print(objeto_full.nombre)
print(objeto_full.depositos)
print(objeto_full.retiros)
print(objeto_full.numeros)
print(objeto_full.pantalla)
print(objeto_full.contraseña)
print(objeto_full.chip)
print(objeto_full.impresora)
print(objeto_full.tarjetas)
print(objeto_full.envios)

