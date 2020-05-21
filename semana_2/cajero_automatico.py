class Cajero:
  #ATRIBUTOS
  nombre="Cajero 1"
  pin="4 digitos"
  dinero="10.00 - 6,000,000.00"
  transferencia="100.000 - 6,000,000.00"
  tarjeta="Debito,credito,ahorro"
  depositos="10.000 - 6,000,000.00"
  retiros="10.000 - 6,000,000.00"
  numeros="0-9"
  pantalla="32 pulgadas"
  teclado="Touch"
  #METODOS
  def retirar(self):
    print("Retirar")
  def abonar(self):
    print("Abonar")
  def encender(self):
    print("Encender")
  def apagar(self):
    print("Apagar")
  def transferir(self):
    print("Transferir")

  def __init_(self):
    print("Cronstructor Cajero Automatico")
  
objeto_cajero= Cajero()
objeto_cajero.retirar()
objeto_cajero.abonar()
objeto_cajero.encender()
objeto_cajero.apagar()
objeto_cajero.transferir()

print(objeto_cajero.nombre)
print(objeto_cajero.transferencia)
print(objeto_cajero.numeros)
print(objeto_cajero.dinero)
print(objeto_cajero.pin)
print(objeto_cajero.tarjeta)
print(objeto_cajero.depositos)
print(objeto_cajero.retiros)
print(objeto_cajero.pantalla)
print(objeto_cajero.teclado)