class Serie():
  #ATRIBUTOS
  temporada= "2da"
  dia="23"
  mes="Enero"
  actor_princiapl="Fernando Rosas"
  actriz="Lucila Mendez"
  #METODOS
  def iniciar(self):
    print("Iniciar")
  def terminar(self):
    print("Terminar")
  def __init__(self):
    print("Constructor Serie de tv")
  
class SerieRomantica(Serie):
 # ATRIBUTOS 
  capitulos="7"
  director="Liyu"
  canal="Netflix"
  duracion="40 minutos"
  tipo="Romantica"

  #METODOS
  def pausar(self):
   print("Pausar")
  def transmitir(self):
   print("Tranferir")
  def __init__(self):
    print("Constructor Serie de tv Romantica")
  
  objeto= Serie()
  objeto.iniciar()
  objeto.terminar()
  print(objeto.temporada)
  print(objeto.dia)
  print(objeto.mes)
  print(objeto.actor_princiapl)
  print(objeto.actriz)

objeto_serie=SerieRomantica()
objeto_serie.iniciar()
objeto_serie.terminar()
objeto_serie.pausar()
objeto_serie.transmitir()
print(objeto_serie.temporada)
print(objeto_serie.dia)
print(objeto_serie.mes)
print(objeto_serie.actor_princiapl)
print(objeto_serie.actriz)
print(objeto_serie.capitulos)
print(objeto_serie.director)
print(objeto_serie.canal)
print(objeto_serie.duracion)
print(objeto_serie.tipo)