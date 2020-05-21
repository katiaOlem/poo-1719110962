class Banco:

  #ATRIBUTOS

  nombre= "BBVA"
  cajeros="10"
  tarjetas=" Debito,Credito,Ahorro "
  horario= " 8:00a.m-10:00p.m "
  lugar= "San Jose"
  direccion= "Encinos #210"
  depositos=" 10.00- 6,000,000 "
  retiros= " 100.00 - 6,000,000 "
  prestamos= " 5,000 - 100,000"
  numero_de_cuenta=" 3 "
  
 #METODOS
  def retirar(self):
    print("Retirar")
  def abonar(self):
    print("Abonar")
  def transferir(self):
    print("Transferir")
  def prestar(self):
    print ("Prestar")
  def cobrar (self):
    print("cobrar")

  def __init__(self):
    print("Constructor Banco")


objeto_un_banco = Banco()

objeto_un_banco.retirar()
objeto_un_banco.abonar()
objeto_un_banco.transferir()
objeto_un_banco.prestar()
objeto_un_banco.cobrar()


print (objeto_un_banco.nombre)
print(objeto_un_banco.cajeros)
print(objeto_un_banco.tarjetas)
print(objeto_un_banco.horario)
print(objeto_un_banco.lugar)
print(objeto_un_banco.direccion)
print(objeto_un_banco.depositos)
print(objeto_un_banco.retiros)
print(objeto_un_banco.prestamos)
print(objeto_un_banco.numero_de_cuenta)








