class Estudiante:
  #ATRIBUTOS
  matricula="171911"
  nombre="Katia"
  carrera= "Tic´s"
  edad="24 años"
  semestre= "2do"
  promedio= "9.5"
  tutor="Oscar"
  direccion="Encinos #255"
  numero="7752021154"
  materia="Programacion (POO)"

  #METODOS
  def elegir(self):
    print("Elegir")
  def asignar(self):
    print("Asignar")
  def obtener (self):
    print("Obtener")
  def avanzar(self):
    print ("Avanzar")
  def reprobar(self):
    print("Reprobar")
  
  def __init__(self):
    print("Constructor Estudiante")
  
objeto_estudiante= Estudiante ()
objeto_estudiante.elegir()
objeto_estudiante.asignar()
objeto_estudiante.obtener()
objeto_estudiante.avanzar()
objeto_estudiante.reprobar()

print(objeto_estudiante.matricula)
print(objeto_estudiante.nombre)
print(objeto_estudiante.carrera)
print(objeto_estudiante.edad)
print(objeto_estudiante.semestre)
print(objeto_estudiante.promedio)
print(objeto_estudiante.tutor)
print(objeto_estudiante.direccion)
print(objeto_estudiante.numero)
print(objeto_estudiante.materia)