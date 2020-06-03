class Banco ():
 #ATRIBUTOS
 nombre="Compartamos"
 horario= " 8:00a.m-10:00p.m "
 direccion= "Encinos #210"
 depositos=" 10.00- 6,000,000 "
 retiros= " 100.00 - 6,000,000 "


 #METODOS
 def retirar(self):
    print("Retirar")
 def abonar(self):
    print("Abonar")
 

 def __init__(self):
    print("Constructor Banco")


 #HERENCIA
class BancoCompartamos (Banco):

  #ATRIBUTOS
  logo="Peces azules y Rosas"
  color="Rosa"
  cajeros="25 Cajeros"
  empleados="29 Empleados"
  computadoras="27 Equipos de Computo"

  def retirar (self): #Polimorfismo
    print(" Retirar desde 7,313 MXN ")
  def abonar (self):
    print(" Abonar desde un Oxxo")
  def transferir (self):
    print("Transferir desde los cajeros")
  def recibir(self):
    print("Recibir de otras tarjetas de Credito & debito")

  def __init__(self):
    print("Constructor Banco Compartamos")

objeto_banco_compartamos= BancoCompartamos()
objeto_banco_compartamos.transferir()
objeto_banco_compartamos.recibir()
objeto_banco_compartamos.retirar()
objeto_banco_compartamos.abonar()
objeto_banco_compartamos.nombre=" Banco Compartamos Tulancingo" #Polimorfismo
print(objeto_banco_compartamos.nombre)
objeto_banco_compartamos.horario="de 10 a.m hasta las 9 p.m"
print(objeto_banco_compartamos.horario)
objeto_banco_compartamos.direccion="Calle Libertad 113 Col. Centro Tulancingo Hgo."
print(objeto_banco_compartamos.direccion)
objeto_banco_compartamos.depositos="maximo 19,501 MXN"
print(objeto_banco_compartamos.depositos)
objeto_banco_compartamos.retiros="7,313 MXN maximo por Operacion"
print(objeto_banco_compartamos.retiros)
print(objeto_banco_compartamos.logo)
print(objeto_banco_compartamos.color)
print(objeto_banco_compartamos.cajeros)
print(objeto_banco_compartamos.empleados)
print(objeto_banco_compartamos.computadoras)