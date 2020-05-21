class Banco:

  #ATRIBUTOS

  nombre: "BBVA"
  cajeros:"10"
  tarjetas:" debito,credito,ahorro "
  horario: " 8:00a.m-10:00p.m "
  lugar:"san jose"
  direccion:"Encinos #210"
  depositos:" 10.00- 6,000,000 "
  retiros: " 100.00 - 6,000,000 "
  prestamos: " 5,000 - 100,000"
  numero_de_cuenta:" 3 "
  
  #METODOS

 def  retirar(self):
   print("Retirar")
   def abonar(self):
     print("Abonar")
     def transferir(self):
       print("Transferir")
       def prestar(self):
         print ("Prestar")
         def cobrar (self):
           print("cobrar")

objeto_banco= Banco()
objeto_banco.retirar()
print objeto_banco.encender()
