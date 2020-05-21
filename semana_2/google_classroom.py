class Classroom ():
  #ATRIBUTOS
  tarea="2"
  mensajes="entregado"
  calificacion="9.5"
  documento="Activida3"
  dia="Martes"
  hora="11:59 p.m"
  codigo="uupia2"
  publicacion="Realiza la activida 3"
  materia="POO"
  alumno="Itzel"

  #METODOS
  def marcar(self):
    print("Marcar")
  def recibir(self):
    print("Recibir")
  def entregar (self):
    print("Entregar")
  def calificar(self):
    print("Calificar")
  def escribir(self):
    print("Escribir")
  def __init__(self):
    print("Constructor Google Classroom")

objeto_classroom= Classroom()
objeto_classroom.marcar()
objeto_classroom.recibir()
objeto_classroom.entregar()
objeto_classroom.calificar()
objeto_classroom.escribir()

print(objeto_classroom.tarea)