class Serie:

  #ATRIBUTOS

  nombre= "Elite"
  dias="Jueves, Viernes"
  horario= " 8:00p.m-10:00p.m "
  actores= "Fernanda,Miriam,Juan,Roberto"
  temporadas= "1-4"
  capitulos= "10"
  director="Fernando de la O"
  tiempo= "un mes"
  calidad="HD"
  canal="HBO"

 
  
 #METODOS
  def comenzar(self):
    print("Comenzar")
  def motivar(self):
    print("motivar")
  def reproducir(self):
    print("Reproducir")
  def terminar(self):
    print ("Terminar")
  def transmitir(self):
    print("Transmitir")

  def __init__(self):
    print("Constructor Serie TV")


objeto_serie_tv = Serie()

objeto_serie_tv.comenzar()
objeto_serie_tv.motivar()
objeto_serie_tv.pausar()
objeto_serie_tv.terminar()
objeto_serie_tv.transmitir()



print (objeto_serie_tv.nombre)
print (objeto_serie_tv.dias)
print (objeto_serie_tv.horario)
print (objeto_serie_tv.actores)
print (objeto_serie_tv.temporadas)
print (objeto_serie_tv.capitulos)
print (objeto_serie_tv.director)
print (objeto_serie_tv.tiempo)
print (objeto_serie_tv.calidad)
print (objeto_serie_tv.canal)