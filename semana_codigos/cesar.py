class CodigoCesar: #Declaracion de la clase
    def __init(self): #Metodo constructor
        pass
    def cifradoDesifrado(self): #Metodo que genera el decifrado y cifrado
        respuesta="S" #variable con la cual el bucle while funcionara
        while respuesta=="S" or respuesta=="s": #si respuesta es S o s el codigo hara lo siguiente
            cifrado = [] #variable la cual ayudara a alamacenar los valores de la cadena
            decifrar = []  #variable la cual ayudara a almacenar el mensaje desifrado
            pregunta=input("Desea Cifrar o Decifrar una cadena? ") #Linea saber que proceso quieres hacer
            if pregunta=="cifrar" or pregunta=="Cifrar": #si es cifrar
                cadena=input("Inserta la cadena a cifrar ") #pide la cadena que se quiere cifrar
                cadena_cifrar=cadena.lower() #convierte todo a minisculas para no tener problemas
                for convertir in cadena_cifrar: #lee la cadena
                    cifrado.append(ord(convertir)) #convierte cada caracter de la cadena en un numero ASCII y la almacena en cifrado
                print("El mensaje cifrado es "+str(cifrado)) #muestra la cadena ya cifrada
                respuesta = input("¿Desea cifrar/descifrar otra cadena s/n?")  # pregunta si quiere repetir el proceso
                if respuesta == "N" or respuesta == "n":  # Si la respuesta es N o n
                    break
            if pregunta=="Decifrar" or pregunta=="decifrar": #si la respuesta es decifrar
                cadena=input("Inserta tu cadena a decifrar ").upper () #pide la cadena que se desea desifrar
                # Abecedario a utilizar en el cifrado
                abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
                
                for i in range(28):
                  descifrado = ""
                    for l in cadena:
       
                        if l in abc:
            pos_letra = abc.index(l)
            # Restamos para movernos a la izquierda
            nueva_pos = (pos_letra - i) % len(abc)
            descifrado += abc[nueva_pos]
        else:
            descifrado+= l
    msj = (f"ROT-{i}:", descifrado)
    print(msj)

                print("Sumensaje decifrado es "+str(decifrar)) #impirme la cadena ya desifrada
                respuesta=input("¿Desea cifrar/descifrar otra cadena s/n?") #pregunta si quiere repetir el proceso
                if respuesta=="N" or respuesta=="n": #Si la respuesta es N o n
                    break #se termina el proceso
objeto_codigo=CodigoCesar() #invocamos al objeto
objeto_codigo.cifradoDesifrado() #Llamamos a su metodo para realizar el codigo.
