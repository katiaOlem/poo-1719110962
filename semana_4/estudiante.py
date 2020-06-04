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
 promedio="9.5"
 beca="Manutencion"
 tutor="Oscar"
 grupo="21"
 nivel_ingles="A3"
 #METODOS
 def elegir(self):
   print("Elegir Carrera de la Universidad")
 def asignar(self):
   print("Asignar su grupo en la Universidad")
 def mantener(self):
   print("Mantener")
 def pasar(self):
   print("Pasar")

 def __init__(self):
   print("Constructor Estudiante Katia")
  

objeto_estudiante_katia=EstudianteKatia()
objeto_estudiante_katia.elegir()
objeto_estudiante_katia.asignar()
objeto_estudiante_katia.mantener()
objeto_estudiante_katia.pasar()
objeto_estudiante_katia.nombre="Katia Itzel Melo Dominguez"
print(objeto_estudiante_katia.nombre)
objeto_estudiante_katia.matricula="1719110962"
print(objeto_estudiante_katia.matricula)
objeto_estudiante_katia.carrera="Ing.Tecnologías de la Información área Desarrollo de Software Multiplataforma-BIS"
print(objeto_estudiante_katia.carrera)
objeto_estudiante_katia.edad="24 años"
print(objeto_estudiante_katia.edad)
objeto_estudiante_katia.semestre="Actualmente 3ero"
print(objeto_estudiante_katia.semestre)
print(objeto_estudiante_katia.promedio)
print(objeto_estudiante_katia.beca)
print(objeto_estudiante_katia.tutor)
print(objeto_estudiante_katia.grupo)
print(objeto_estudiante_katia.nivel_ingles)
