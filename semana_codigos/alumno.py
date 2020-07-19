r="s" #variable para ayudar al ciclo while
datos = [] #Variable que alamacenara los datos de los Alumnos
class Alumno: #Clase
    def __init__(self): #Metodo
        pass
    def datos(self): #Metodo de los Datos de los Alumnos
        nombre_alumno=input("Ingrese el Nombre Completo del Alumno= ") #Variable del Nombre del Alumno
        año_del_alumno=int(input("Ingrese el Año de Nacimeinto del Alumno: ")) #Variable de la Fecha de Nacimeinto del Alumno
        grupo_del_alumno=input("Ingrese el Grupo del Alumno= ") #pide el grupo del alumno
        año_alumno=2020-año_del_alumno #Formula que nos ayudara a calcular la edad actual de cada Alumno
        datos.append("La edad del alumn@ "+str(nombre_alumno)+" es de "+str(año_alumno)+" años") #Variable que nos ayudara a Remplazar los datos almacenados en una forma Agradable
    def imprimir(self): #Metodo para Imprimir en la pantalla
        for leer in datos: #Leer Ayudara a Leer los Datos Almacenados en Datos
            print(leer) #Imprimira los Datos Con La variable Datos. append
while r=="s" or r=="S": #Condicion para seguir el programa 
    objecto_Almuno=Alumno() #Objeto de la Clase 
    objecto_Almuno.datos()#Objeto de los Datos
    r=input("¿Desea leer otro alumno? s/n ") 
    if r=="N" or r=="n": #Si la Respuesta es N VS n ENTONCES EL PROGRAMA 
        objecto_Almuno.imprimir() #iMPRIMIRA LOS DATOS EN LA PANTALLA Y 
        break # FINALIZARA