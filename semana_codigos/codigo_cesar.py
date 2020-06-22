class CodigoCesar: #CLASE
    def __init__(self): #CONSTRUCTOR
        self.texto=input(" Ingrese la cadena= ")
    
    def descifrar (self):
      descifrar_texto=input(" Ingrese la cadena a descifrar= ")
      for caracter in self.texto:
        descifrar=ord(caracter)
        descifrar=ord(decifrar-3)
        descifrar_texto=descifrar_texto+caracter.replace(caracter,descifrar)
        print("El texto decifrado es= "+str(descifrar_texto)
        
    def cifrar (self):
      cifrar_texto= int(input(" Ingrese el texto que desea Cifrar= "))
      for caracter in self.texto:
        cifrar=ord(caracter)
        cifrar=chr(cifrar+3)
        cifrar_texto=cifrar_texto+caracter.replace(caracter,cifrar)
      print("El texto cifrado es= "+str(cifrar_texto)
      

while True:
  objeto= CodigoCesar()
  print("cifrar")
  print("descifrar")
  r=int(input("Quiere cifrar o descifrar una cadena:"))
  if r== cifrar():
    objeto.cifrar
  elif r==descifrar():
    objeto.descifrar()
  else:
    print(Fin)


  pregunta=input("¿Desea cifrar/descifrar otra cadena s/n?:")

  if not (pregunta=="S" or pregunta== "s"):
    break #Finaliza