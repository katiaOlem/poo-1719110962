class Estudiante:
  #ATRIBUTOS
  nombre="Katia"
  matricula="171911"
  carrera= "Tic´s"
  edad="24 años"
  semestre= "2do"

   #METODOS
  def elegir(self):
    print("Elegir")
  def asignar(self):
    print("Asignar")

  def __init__(self):
    print("Constructor Estudiante")

  #HERENCIA
class EstudianteKatia (Estudiante):
  #ATRIBUTOS
 matricula="171911"
 carrera="Tic´s Bis"
 edad="24"
 semestre="3ero"
 promedio="9.5"
 beca="Manutencion"
 tutor="Katia"
 grupo="21"
 nivel_ingles="A3"
 estado_civil="Casada"
 #METODOS

 def elegir(self):
    print("Elegir")
 def asignar(self):
    print("Asignar")
 def mantener(self):
   print("Mantener")
 def pasar(self):
   print("Pasar")
 def __init__(self):
   print("Constructor EstudianteKatia")
  
objeto= Estudiante()
objeto.elegir
objeto.asignar
print(objeto.nombre)
print(objeto.matricula)
print(objeto.carrera)

