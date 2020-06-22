class CodigoCesar: #Declaracion de la clase
    def __init(self): #Metodo constructor
        pass
    def Cifrado(self): #Metodo
        r="S" 

while r=="S" or r=="s": #si respuesta es S o s el codigo hara lo siguiente
            cifrado =ord (caracter) #variable del cifrado
            cifrado=chr(caracter+3)

            pregunta=input("Desea Cifrar o Decifrar una cadena? ") # Metodo para elegir que funcion desea 
            
            if pregunta=="cifrar" or pregunta=="Cifrar": #id de la funcion cifrar
                cadena=input("Inserta la cadena a cifrar ") #Ingresa la cadena a decifrar
            for caracter in self.cadena:
              cifrado=cifrado+caracter.replace(caracter,cifrado)
              r = input("¿Desea cifrar/descifrar otra cadena s/n?")  # pregunta si quiere repetir el proceso
            if r == "N" or r == "n":  
                    break
        
            if pregunta=="Decifrar" or pregunta=="decifrar": 
              def decifrado (self):
                cadena=input("Inserta tu cadena a decifrar ") #Inserta la cadena a decifrar
            for caracter in self.cadena:
                



         respuesta=input("¿Desea cifrar/descifrar otra cadena s/n?") 
         if respuesta=="N" or respuesta=="n": 
                 break #Finaliza
objeto_codigo=CodigoCesar() 
objeto_codigo.CifradoDesifrado() 