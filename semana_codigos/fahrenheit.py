class Temperaturas:#Clase
    def __init__(self): #Metodo constructor
        pass
    def TotalTemperaturas(self):#Metodo de Temperaturas
        grados_centigrados=[] #Variable que nos permitira Almacenar los Grados Centigrados
        grados_fahrenheit=[]#Variable que Almacenara Grados Fahrenheit
        r="S"#Variable de Respuesta para que este se repita 
        contador=0 #Varible que nos contara el Total de veces que se hará el programa 
        while r=="S" or r=="s": #si respuesta es S vs s el programa seguira 
            contador+=1 #La variable contador se sumara +1
            temperatura=int(input("Inserte la temperatura en grados Centigrados= ")) #Variable que nos permitira Poner los Grados Centigrados que se desean Convertir 
            grados_centigrados.append(temperatura) #Variable que se almacena para que esta pueda ser analizada 
            convertir=((temperatura)*(9/5))+32 #Formula que permite convertir la temperatura de centigrados a fahrenheit
            grados_fahrenheit.append(convertir) #variable que alamacenara los grados Fahrenheit
            r=input("¿Desea convertir otra temperatura de grados Centigrados a Fahrenheit? ") #Variable que nos permitira repetir el programa 
            if r=="N" or r=="n": #si la se respuesta es N vs n Finaliza el Programa 
                editar=open("temperaturas.txt","a") #Variable que nos permitira abrir el documento donde con "a" sera posible editar y guardara las temperaturas agregadas en este programa  a=append
                editar.write("Totales \n") #Variabe que nos permitira escribir
                editar.write("El total de las temperaturas analizadas en grados Centigrados son=  "+str(grados_centigrados)+"\n") #Imprimira las temperaturas que se guardaron en este programa en el documento abierto.
                editar.write("El total de las temperaturas convertidas a grados Fahrenheit "+str(grados_fahrenheit)+"\n")#Imprime las temperaturas convertidas en grados Fahrenheit en el documento abierto
                promedio_total=sum(grados_centigrados)/contador # Variable que nos sumara todas las temperaturas de grados centigrados 
                promedio_total_fahrenheit=sum(grados_fahrenheit)/contador#Variable que nos sumara todas las temperaturas de grados Fahrenheit
                editar.write("El Promedio Total de las temperatura en grados Centigrados son= "+str(promedio_total)+"\n")#Escribira en el documento abierto el Promedio Total de los grados Centigrados 
                editar.write("El promedio de las temperaturas en grados Fahrenheit son= "+str(promedio_total_fahrenheit)+"\n")#Escribira en el documento abierto el Promedio Total de los grados Fahrenheit
                editar.close()#Variable que nos permite cerrar el Documento
                 
                print("El Promedio Total de las temperaturas en Grados Centigrados son= "+str(promedio_total))#Imprime Elpromedio Total de los grados Centigrados 
                print(" El Promedio Total de las Temperaturas en Grados Fahrenheit son= "+str(promedio_total_fahrenheit)) #Imprime Elpromedio Total de los grados Fahrenheit
                break #Finaliza el programa 

objeto_Temperaturas=Temperaturas() #objeto de Class
objeto_Temperaturas.TotalTemperaturas() #objeto de def