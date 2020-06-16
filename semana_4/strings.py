class Mensaje: #Clase
  def __init__(self): 
    pass
  def bucleWhile(self): #Bucle
    r="S"
    while r=="S" or r=="s": #Respuesta
      cadena=input() #Insertar el Mensaje
      print(cadena) #imprime el Mensaje
      print(len(cadena)) #numero de caracteres 
      print(cadena.replace(" ", "")) #elimina los espacios
      print(cadena.lower()) #Convierte en Minusculas
      print(cadena.upper()) #Convierte en Mayusculas
      print(cadena.split(" "))#Separa el mensaje por partes

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
