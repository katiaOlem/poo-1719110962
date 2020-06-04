class Coche():
  #atributos
 color= "Azul"
 marca= "Jetta"
 placas= "auM-bc"
 llantas= "4"
 motor= "Automatico"

 # METODOS
 def chocar(self):
    print("Chocar")
 def frenar(self):
    print("Frenar")
 def __init__(self):
    print("Constructor Carro")
 
class CocheAzul(Coche):

 #ATRIBUTOS
 asientos= "6 dos delanteros 4 traseros"
 espejos= "Laterales"
 usb= "2"
 pantallas= "1 thouch"
 rines="4"

 #METODOS

 def chocar(self):
    print("Chocar puede ser por que el chofer se quedo dormido, o biene en estado de ebriedad")
 def frenar(self):
    print("Frenar con el freno de mano de su Carro")
 def acelerar(self):
   print("Acelerar")
 def fallar(self):
    print("Fallar")
 def __init__(self):
   print("Constructor Carro Azul")

objeto_coche= CocheAzul()
objeto_coche.chocar()
objeto_coche.frenar()
objeto_coche.acelerar()
objeto_coche.fallar()
objeto_coche.color="Color Azul con franjas Blancas"
print(objeto_coche.color)
objeto_coche.marca="Jetta 2da Generacion"
print(objeto_coche.marca)
objeto_coche.placas="Del estado de Mexico WLu-94-69"
print(objeto_coche.placas)
objeto_coche.llantas="Llantas de la marca Michelin"
print(objeto_coche.llantas)
objeto_coche.motor="Motor de diésel"
print(objeto_coche.motor)
print(objeto_coche.asientos)
print(objeto_coche.espejos)
print(objeto_coche.usb)
print(objeto_coche.pantallas)
print(objeto_coche.rines)


