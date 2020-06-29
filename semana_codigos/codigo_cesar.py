class CodigoCesarArchivos: #Clase 
    def __init__(self): #Metodo
        pass
    def cifradoDesifrado(self):
        r="S" #Respuesta
        while r=="S" or r=="s": #Respuesta es s vs S para seguir el programa
            cifrado = "" #variable de Cifrado
            descifrado = "" #variable del Decifrado
            archivo = input("Nombre del archivo y que desea analizar ") #linea para escribir el nombre del archivo que desea analizar
            abrir = open(archivo, "r") #Variable de Lectura 
            leer = abrir.read() #Variable que permitira leer cada linea en el archivo
            print(leer)#Imprimira el contenido del archivo
            pregunta = input("¿Desea realizar cifrado o descifrado? ") #pregunta 
            if pregunta == "cifrado" or pregunta == "Cifrado": #si es cifrar
                abrir = open(archivo, "w") #Variable que abrira el archivo y nos permitira modificar el texto del archivo
                for scannear in leer: #Lee el archivo 
                    alfabeto = ord(scannear) #Codigo ASCII
                    cifrado += chr(alfabeto - 3)#Se le resta al codigo ASCII 3 para cifrar el texto del archivo
                abrir.write(cifrado) #se cifra el archivo rescribiendo el cifrado
                print(cifrado) #Imprira el cifrado que se le dio al texto del archivo abierto
                abrir.close()# cierra el archivo
            if pregunta == "Descifrado" or pregunta == "descifrado": #si es descifrar
                abrir = open(archivo, "w") #variable que abre al archivo para sustituir el texto
                for scannear in leer: #lee archivo 
                    alfabeto = ord(scannear)#convierte cada variable en el archivo en codigo ASCII
                    descifrado += chr(alfabeto + 3)#Se sumaran 3 y los convertira en cada caracter para que el texto vuelva a tener sus mismas variables o vs
                abrir.write(descifrado+ "\n ") #Variable que permitira escribir en el texto del archivo y se guarde
                abrir.close()# variable que permitira cerrar el archivo de texto
                print(descifrado)#Imprime el archivo descifrado
            r=input("Desea realizar cifrado o desifrado de  otro archivo? ") #pregunta si desea analizar otro archivo de texto
            if r=="N" or r=="N": #Respuesta es N Vs n
                break #Fin del codigo
objeto_cifrado=CodigoCesarArchivos() #objeto de la clase
objeto_cifrado.cifradoDesifrado() #objeto del  metodo
