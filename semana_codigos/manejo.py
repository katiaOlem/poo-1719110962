import math
lista_numeros=[]#Contador de los números


class NumerosError ():#Clase
    def __init__(self): #Metodo Constructor
        pass
    def numeros_evaluar(self): #definimod un metodo para pedir los numeros
        try:
            numeros=int(input(" Ingrese el total de numeros que desea evaluar=     "))

            for i in range (numeros):
                numero=int(input("Ingrese el numero que desea evaluar=   "))
                lista_numeros.append (numero)
            
        except Exception as error: #si detecta algun error
            print("Verifique los datos ingresados",error.args) #imprime la siguiente linea
            
    def Indice_numeros(self): #metodo que hara lo siguiente
    
        r="S" #ayudara al ciclo while
        try: #ayudara a detectar un error
            while r == "s" or otra == "S": #mietras while sea S
                indice=int(input(" introduza un índice "))#Pide insertar un numero en de indice
                seletion=lista_numeros[indice]#seleccionara el valor almacenado en ese indice
                print(seletion) #imprime el valor que seleccionaste
                raiz_cuadrada=math.sqrt(seletion)#el numero seleccionado calcula la raiz cuadrada
                print("La raiz cuadra del numero es= "+str(raiz_cuadrada)) #imprime la raiz cuadrada
                cubo=(seletion + seletion + seletion) #el indice selccionado lo elevera al cubo
                print("El numero elevado al cubo es= "+str(cubo))#imprime el resultado del indice elevado al cubo
                if seletion%2==0:#si el indice seleccionado es divicible entre dos y su reciduo final es 0
                    print("El numero que Ingreso es PAR")#imprime la siguiente linea
                else: #de lo contrario
                    print("El numero que ingreso es IMPAR") #imprime lo siguiete 
                otra=input("¿Desea realizar otro calculo? s/n ") #si desea realizar otro calculo
                if r=="n" or r=="N": #si la respuesta es N o n
                    break #termina el codigo
        except Exception as error: #si detecta algun error
            print("Verifique los datos ingresados",error.args)

obj=NumerosError ()
obj.numeros_evaluar()#llamamos a nuetrso primero metodo
obj.Indice_numeros()#llamamos a nuestro segundo metodo