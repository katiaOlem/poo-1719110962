class Palindromo: #Clase
    def __init__(self):
      pass
    def texto(self): 
      r="S"
      while r=="S" or r=="s":
       frase = input(" Ingrese el texto que desea analizar = ") #Insertara Texto
       texto = frase.lower() #Minusculas
       total_de_espacios=0 #Conteo de los espacios
       for espacios in texto: # Analizara la cadena para obtener los espacios
          if espacios in " ": 
            total_de_espacios+=1 #Obtendra el total de espacios
       print(total_de_espacios) #Imprimira el total de los espacios
            
       frase = frase.lower()  # Convierte el texto a Minusculas
       print(frase)
       frase = frase.replace(" ", "")  # Elimina los espacios que tenga el texto
       frase=frase.replace(".", "") #Elimina los caracteres que pueda tener el texto
       frase=frase.replace("á","a")  #Reemplaza la Tilde
       frase = frase.replace("é", "e") #Reemplaza la Tilde
       frase = frase.replace("í", "i") #Reemplaza la Tilde
       frase = frase.replace("ó", "o") #Reemplaza la Tilde 
       frase= frase.replace("ú", "u") #Reemplaza la Tilde
       print(frase) #Imprime el texto sin espacios, ni caracteres, ni tildes para leer si es Palindromo el texto
       contador_de_vocales=0 #contara el numero de vocales en la frase 
       for vocales in frase:
          if vocales in "aeiou":
            contador_de_vocales+=1

       print(contador_de_vocales) #Imprimira el total de las vocales
       inversa=""

       for i in frase: #Permitira obtener el texto modificado
            inversa= i + inversa # Es la manera en que nos permitira leer el texto a la inversa y saber si el texto es Palindromo 
       if inversa==frase:
              print("El texto que Ingreso es Palindromo")
       else:
              print("El texto que Ingreso no es Palindromo")

       r=input("¿Desea analizar otra cadena s/n?")#Si la respuesta es "S" or "s" volvera a analizar otro dato
       if r=="N" or r=="n": #Si la respuesta es "N" or "n"se termina el programa.
           break

objeto_palindromo=Palindromo() 
objeto_palindromo.texto()
