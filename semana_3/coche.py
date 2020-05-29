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
 asientos= "6"
 espejos= "Laterales"
 usb= "2"
 panatallas= "1 thouch"
 rines="4"

 #METODOS

 def acelerar(self):
   print("Acelerar")
 def fallar(self):
    print("Fallar")
 def __init__(self):
   print("Constructor Carro Azul")


objeto= Coche()
objeto.chocar()
objeto.frenar()
print(objeto.color)
print(objeto.marca)
print(objeto.placas)
print(objeto.llantas)
print(objeto.motor)

objeto_coche= CocheAzul()
objeto_coche.chocar()
objeto_coche.frenar()
objeto_coche.acelerar()
objeto_coche.fallar()
print(objeto_coche.color)
print(objeto_coche.marca)
print(objeto_coche.placas)
print(objeto_coche.llantas)
print(objeto_coche.motor)
print(objeto_coche.asientos)
print(objeto_coche.espejos)
print(objeto_coche.usb)
print(objeto_coche.panatallas)
print(objeto_coche.rines)


