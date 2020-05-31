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
 def mantener(self):
   print("Mantener")
 def pasar(self):
   print("Pasar")

 def __init__(self):
   print("Constructor Estudiante Katia")
  
objeto= Estudiante()
objeto.elegir()
objeto.asignar()
print(objeto.nombre)
print(objeto.matricula)
print(objeto.carrera)
print(objeto.edad)
print(objeto.semestre)

objeto_estudiante_katia=EstudianteKatia()
objeto_estudiante_katia.elegir()
objeto_estudiante_katia.asignar()
objeto_estudiante_katia.mantener()
objeto_estudiante_katia.pasar()
print(objeto_estudiante_katia.nombre)
print(objeto_estudiante_katia.matricula)
print(objeto_estudiante_katia.carrera)
print(objeto_estudiante_katia.edad)
print(objeto_estudiante_katia.semestre)
print(objeto_estudiante_katia.promedio)
print(objeto_estudiante_katia.beca)
print(objeto_estudiante_katia.tutor)
print(objeto_estudiante_katia.grupo)
print(objeto_estudiante_katia.nivel_ingles)
