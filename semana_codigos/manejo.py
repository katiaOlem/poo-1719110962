import math #Ayuda con las funciones matemáticas
lista_numeros=[]#Contador de los números


class NumerosError ():#Clase
    def __init__(self): #Metodo Constructor
        pass
    def numeros_evaluar(self): #Metodo 
        try:#Declaracion de Try  para identificar errores 
            numeros=int(input(" Ingrese el total de numeros que desea evaluar =   ")) #Variable del # de  numeros que deseamos evaluar y realizar las siguientes operaciones.

            for i in range (numeros):#EL rango de los  numeros
                numero=int(input("Ingrese el numero que desea evaluar =   ")) #Variable que nos permite Ingresar los numeros a evaluar 
                lista_numeros.append (numero) #Reemplazaremos los numeros en el contador de la lista_numeros
            
        except Exception as error: # Except captura el error
            print("!!!   ERROR   !!!",error.args) 
            
    def Indice_numeros(self): #Metodo del indice 
    
        r="s" or "S" #Respuesta S OR s 
        try: #Declaracion de Try  para identificar errores
            while r == "s" or r == "S": #Si la respuesta es S OR s el programa realizara Lo siguiente 
                indice=int(input(" Introduza un índice =  "))#Variable que nos permite Ingresar el # del Indice que deseamos Imprimir con las operaciones qu estan a continuacion
                seletion=lista_numeros[indice]#Variable que seleccionara el Indice de los numeros agregados para evaluar
                print(seletion) #Imprimira el valor seleccionado

                raiz_cuadrada=math.sqrt(seletion)#Math sqrt nos permite sacar la raiz del numero seleccionado
                print("Su Raiz Cuadrada es=  "+ str (raiz_cuadrada)) #imprime la raiz cuadrada del numero seleccionado 
                cubo=(seletion * seletion * seletion) #El numero seleccionado se elebara al cubo
                print("Elevado al cubo es= "+ str (cubo))#imprime el resultado elevado al cubo
                if seletion == 0:# Si el numero es = a 0 el numero es par 
                   print ("Este número es par=  ") #Imprime el mensaje 
                elif seletion%2 == 0: #si el numero es divisible hasta o es numero par 
                  print ("El numero es par") #Imprime
                else:
                  print ("El numero es impar ") # Si no es impar 
                  
                r=input(" ¿Desea realizar otro calculo? s/n ") #Varible de respuesta para saber si regresa al ciclo o termina el prgrama 
                if r=="n" or r=="N": #si la respuesta es N o n
                    break #Finaliza
        except Exception as error: #Except captura el error
            print(" !! ERROR !!",error.args) #Imprime el error 

obj=NumerosError ()#Objeto de la Class 
obj.numeros_evaluar()#Objeto del Metodo de numeros_evaluar
obj.Indice_numeros()#Objeto del Metodo de Indice_numeros