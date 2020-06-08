class Mensaje: #Clase
  def __init__(self): 
    pass
  def bucleWhile(self): #Bucle
    r="S"
    while r=="S" or r=="s": #Respuesta
      cadena=input() #Insertar el Mensaje
      print(cadena) #imprime el Mensaje
      print(len(cadena)) #numeo de caracteres 
      print(cadena.replace(" ", "")) #elimina los espacios
      print(cadena.lower()) #Convierte en Minusculas
      print(cadena.upper()) #Convierte en Mayusculas
      print(cadena.split(" "))#Separa el mensaje por partes
      print(cadena[0])
      print(cadena[1])
      print(cadena[2])
      print(cadena[3])
      print(cadena[4])
      print(cadena[5])
      print(cadena[6])
      print(cadena[7])
      print(cadena[8])
      print(cadena[9])
      print(cadena[10])
      print(cadena[11])
      print(cadena[12])
      print(cadena[13])
      print(cadena[14])
      print(cadena[15])
      print(cadena[16])
      print(cadena[17])
      print(cadena[18])
      print(cadena[19])
      print(cadena[20])
      print(cadena[21])
      print(cadena[22])
      print(cadena[23])
      print(cadena[24])
      print(cadena[25])


      if cadena.isalpha()==True or cadena.islower()==True or cadena.istitle()==True: #Cadena
        print("El Mensaje es un tipo cadena")
      if cadena.isdigit()==True: #Numerico
        print("El Mensaje es un tipo numerico")
      if cadena.isdecimal()==True: #Decimal
        print("El mensaje es tipo decimal")
    
      r=input("¿Desea analizar otra cadena s/n?")#Si la respuesta es "S" or "s" volvera a analizar otro dato
      if r=="N" or r=="n": #Si la respuesta es "N" or "n"se termina el programa.
        break
objeto_cadena=Mensaje() 
objeto_cadena.bucleWhile()
