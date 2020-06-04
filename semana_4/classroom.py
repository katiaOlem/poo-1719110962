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
 def calificar(self):
   print("Calificar la tarea de los Alumnos, por los Profesores")
 def enviar (self):
   print("Enviar las tareas y tambien comentarios")
 def llamar(self):
   print("Llamar por telefono y con la aplicacion desde celular o computadora")
 def transmitir(self):
    print("Transmitir la pantalla para todos en la videollamada")

 def __init__(self):
   print("Construtor Google Classroom Meet")


objeto_meet=ClassroomMeet()
objeto_meet.calificar()
objeto_meet.enviar()
objeto_meet.llamar()
objeto_meet.transmitir()
objeto_meet.codigo="Proporsionado por la pagina de Meet"
print(objeto_meet.codigo)
objeto_meet.publicacion="Publicaciones para recordar las videollamadas en el grupo de Classroom"
print(objeto_meet.publicacion)
objeto_meet.materia="Materia creada por los Docentes"
print(objeto_meet.materia)
objeto_meet.alumno="Nombre completo del Alumno"
print(objeto_meet.alumno)
objeto_meet.tarea="Tareas asignadas por los Docentes para los alumnos"
print(objeto_meet.tarea)
print(objeto_meet.llamadas)
print(objeto_meet.mensajes)
print(objeto_meet.imagenes)
print(objeto_meet.videos)
print(objeto_meet.audio)