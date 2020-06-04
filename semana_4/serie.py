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
  def iniciar (self):
    print("Iniciar la Primer Temporada de la Serie LOVE ")
  def terminar(self):
    print("Terminar la Primer Temporada de la Serie LOVE ")
  def pausar(self):
   print("Pausar")
  def transmitir(self):
   print("Tranferir")
  def __init__(self):
    print("Constructor Serie de tv Romantica")

objeto_serie=SerieRomantica()
objeto_serie.iniciar()
objeto_serie.terminar()
objeto_serie.pausar()
objeto_serie.transmitir()
objeto_serie.temporada="La primer Temporada de la Serie Romantica LOVE"
print(objeto_serie.temporada)
objeto_serie.dia="La serie  LOVE se Estrena el dia 25"
print(objeto_serie.dia)
objeto_serie.mes="mes de Julio"
print(objeto_serie.mes)
objeto_serie.actor="Actor principal David Kingove"
print(objeto_serie.actor_princiapl)
objeto_serie.actriz="Actriz principal Lesley Arfin"
print(objeto_serie.actriz)
print(objeto_serie.capitulos)
print(objeto_serie.director)
print(objeto_serie.canal)
print(objeto_serie.duracion)
print(objeto_serie.tipo)