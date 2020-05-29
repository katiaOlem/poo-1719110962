class Classroom():
  #ATRIBUTOS
  codigo="uupia2"
  publicacion="Realiza la activida 3"
  materia="POO"
  alumno="Itzel"
  tarea="Herencia"
 #METODOS
  def calificar(self): 
   print("Calificar")
  def enviar(self):
   print("Enviar")
  def __init__(self):
    print("Constructor Google Cassroom")

#HERENCIA
class ClassroomMeet(Classroom):
 #ATRIBUTOS
 llamadas="Grupales"
 mensajes="En grupo y Privados"
 imagenes="Transmitidas por el Profesor"
 videos="Transmitidas por el Profesor"
 audio="transmmitido por Profesores y Alumnos"

 #METODOS
 def llamar(self):
   print("Llamar")
 def transmitir(self):
  print("Transmitir")
 def __init__(self):
   print("Construtor Google Classroom Meet")

objeto= Classroom()
objeto.calificar()
objeto.enviar()
print(objeto.codigo)
print(objeto.publicacion)
print(objeto.materia)
print(objeto.alumno)
print(objeto.tarea)

objeto_meet=ClassroomMeet()
objeto_meet.calificar()
objeto_meet.enviar()
objeto_meet.llamar()
objeto_meet.transmitir()
print(objeto_meet.codigo)
print(objeto_meet.publicacion)
print(objeto_meet.materia)
print(objeto_meet.alumno)
print(objeto_meet.tarea)
print(objeto_meet.llamadas)
print(objeto_meet.mensajes)
print(objeto_meet.imagenes)
print(objeto_meet.videos)
print(objeto_meet.audio)