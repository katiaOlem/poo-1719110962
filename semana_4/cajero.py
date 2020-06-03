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
  contrasena="18965"
  chip="si"
  impresora="Matricial"
  tarjetas="Debito, Credito"
  envios="Toda la Republica"

  #METODOS
  def retirar(self):
    print("Retirar dinero de 100 MXN minimo")
  def extraer (self):
    print("Extraer el dinero del cajero con su tarjeta")
  def abonar(self):
   print("Abonar")
  def recargar(self):
   print("Recargar ")
  def __init__(self):
    print("Constructor Cajero Automatico Full")

objeto_full=CajeroFull()
objeto_full.retirar()
objeto_full.extraer()
objeto_full.abonar()
objeto_full.recargar()
objeto_full.nombre="Cajero Automatico de BBVA"
print(objeto_full.nombre)
objeto_full.depositos="Depositos de 100 MXN minima hasta 9500 MXN maxima"
print(objeto_full.depositos)
objeto_full.retiros="Desde su app con y sin Tarjeta"
print(objeto_full.retiros)
objeto_full.numeros="del 0 al 9 Touch"
print(objeto_full.numeros)
objeto_full.pantalla="llamada touchscreen"
print(objeto_full.pantalla)
print(objeto_full.contrasena)
print(objeto_full.chip)
print(objeto_full.impresora)
print(objeto_full.tarjetas)
print(objeto_full.envios)