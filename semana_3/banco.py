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
  nombre=("CompartamosBanco")
  horario="7:00a.m-9:00p.m"
  lugar="Mateos"
  direccion="Rubi #215"
  depositos="10.00-6,000,000"
  retiros="10.00-6,000,000"
  logo="Casa"
  color="Azul"
  cajeros="25"
  empleados="29"
  

  def retirar(self):
    print("Retirar")
  def abonar(self):
    print("Abonar")
  def transferir (self):
    print("Transferir")
  def recibir(self):
    print("Recibir")

  def __init__(self):
    print("Constructor BancoCompartamos")


objeto= Banco()

objeto.retirar()
objeto.abonar()
print(objeto.nombre)
print(objeto.horario)
print(objeto.direccion)
print(objeto.depositos)
print(objeto.retiros)

objeto_banco_compartamos= BancoCompartamos()
objeto_banco_compartamos.retirar()
objeto_banco_compartamos.abonar()
objeto_banco_compartamos.transferir()
objeto_banco_compartamos.recibir()
print(objeto_banco_compartamos.nombre)
print(objeto_banco_compartamos.horario)
print(objeto_banco_compartamos.lugar)
print(objeto_banco_compartamos.direccion)
print(objeto_banco_compartamos.depositos)
print(objeto_banco_compartamos.retiros)
print(objeto_banco_compartamos.logo)
print(objeto_banco_compartamos.color)
print(objeto_banco_compartamos.cajeros)
print(objeto_banco_compartamos.empleados)
