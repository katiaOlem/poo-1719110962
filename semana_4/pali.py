class Palindromo: #Clase
    def __init__(self):
      pass
    def texto(self): 
      r="S"
      while r=="S" or r=="s":
       frase = input("Ingresa el texto que desea analizar= ") #Insertara Texto
       texto = frase.lower()
       total_de_espacios=0 #Conteo de los espacios
       for espacios in texto: # Analizara la cadena para obtener los espacios
          if espacios in " ": 
            total_de_espacios+=1 #Obtendra el total de espacios
       print(total_de_espacios) #Imprimira el total de los espacios
            
       frase = frase.lower()  # Convierte el texto a Minusculas
       print(frase)
       frase = frase.replace(" ", "")  # elimina los espacios que tenga el texto
       frase=frase.replace(".", "")
       frase=frase.replace("á","a") 
            #reemplazan las letras con tilde por una sin tilde
       frase = frase.replace("é", "e")
       frase = frase.replace("í", "i")
       frase = frase.replace("ó", "o")
       frase= frase.replace("ú", "u")
       print(frase)
       contador_de_vocales=0
       for vocales in frase: #contara los caracteres
          if vocales in "aeiou":
            contador_de_vocales+=1

       print(contador_de_vocales)
       inversa=""

       for i in frase: #Permitira obtener la letra de la cadena 
            inversa= i + inversa # Obtendremos laultimaletra de la palabra o frase
       if inversa==frase:
              print("El texto que Ingreso es Palindromo")
       else:
              print("El texto que Ingreso no es Palindromo")

       r=input("¿Desea analizar otra cadena s/n?")#Si la respuesta es "S" or "s" volvera a analizar otro dato
       if r=="N" or r=="n": #Si la respuesta es "N" or "n"se termina el programa.
           break

objeto_palindromo=Palindromo() 
objeto_palindromo.texto()
