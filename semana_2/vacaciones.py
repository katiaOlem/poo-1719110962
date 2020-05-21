class Vacaciones:

#ATRIBUTOS

 lugar= " Paris "
 dia= "5"
 hora= " 2:00 p.m"
 tiempo= "3 dias"
 personas="3"
 transporte="Auto"
 maletas="5"
 tramite="Reservación"
 dinero="8,000.00"
 hotel="4 STARS"

#METODOS
 def relajar(self):
   print("Relajar")
 def transportar(self):
   print("Transportar")
 def visitar (self):
   print("Visitar")
 def descansar (self):
   print("Descansar")
 def disfrutar(self):
   print ("Disfrutar")

 def __init__(self):
   print("Construccion Vacaciones")
  
objeto_vacaciones= Vacaciones()

objeto_vacaciones.relajar()
objeto_vacaciones.transportar()
objeto_vacaciones.visitar()
objeto_vacaciones.descansar()
objeto_vacaciones.disfrutar()

print(objeto_vacaciones.lugar)
print(objeto_vacaciones.dia)
print(objeto_vacaciones.hora)
print(objeto_vacaciones.tiempo)
print(objeto_vacaciones.personas)
print(objeto_vacaciones.transporte)
print(objeto_vacaciones.maletas)
print(objeto_vacaciones.tramite)
print(objeto_vacaciones.dinero)
print(objeto_vacaciones.hotel)
