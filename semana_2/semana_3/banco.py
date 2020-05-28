class Banco ()
 #ATRIBUTOS
 horario= " 8:00a.m-10:00p.m "
 lugar= "San Jose"
 direccion= "Encinos #210"
 depositos=" 10.00- 6,000,000 "
 retiros= " 100.00 - 6,000,000 "


 #METODOS
 def retirar(self):
    print("Retirar")
  def abonar(self):
    print("Abonar")
  def transferir(self):
    print("Transferir")

  def __init__(self):
    print("Constructor Banco")


 #HERENCIA
class BancoCompartamos Banco(): 
  #ATRIBUTOS
  horario="7:00a.m-9:00p.m"
  lugar="Mateos"
  direccion="Rubi #215"
  depositos="10.00-6,000,000"
  retiros="10.00-6,000,000"
  logo="Casa"
  color="Azul"
  cajeros="25"
  empleados="29"
  computadoras="25"

  def retirar(self):
    print("Retirar")
  def transferir (self):
    print("Transferir")
  def abonar(self):
    print("Abonar")
  def recibir(self):
    print("Recibir")
  def consultar(self):
    print("Consultar")
 def __init__(self):
    print("Constructor BancoCompartamos")

objeto_banco_compartamos= BancoCompartamos()