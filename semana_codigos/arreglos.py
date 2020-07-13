contador = 0  #variable del contador
class Temperaturas:#Clase

  promedio_total=0 #Variable que Ayuda ha almacenar el Promedio de Grados Centigrados
  promedio_total_fahrenheit=0 #Variable que Ayuda ha almacenar el Promedio de Grados  fahrenheit
  fecha=[] #Variable donde se almacenara las fechas Ingresadas
  grados_centigrados=[] #Variable donde se almacenara los grados centigrados
  grados_fahrenheit=[] #Variable donde se almacenara los grados centigrados a Fahrenheit


  def __init__(self): #Metodo constructor
        pass

  def FechasTemperaturas(self):#Metodo de Registro 
    fecha=input("Ingrese la Fecha= ") #Variable que permitira que se agregue la Fecha
    self.fecha.append(fecha) #Append permite que las fechas Ingresadas valla a la Variable (fechas) que almacena Las Fechas
    temperatura=int(input("Ingrese la Temperatura en Grados Centigrados= "))#Variable que nos permitira Poner los Grados Centigrados que se desean Convertir 
    self.grados_centigrados.append(temperatura) #Variable que nos permitira almacenar los grados centigrados convertidos en Fahrenheit

    convertir=((temperatura)*(9/5))+32 #Formula que permite convertir la temperatura de centigrados a fahrenheit

    self.grados_fahrenheit.append(convertir) #variable que alamacenara los grados Fahrenheit
  def ConvierteyBusca(self): #Metodo convertir y buscar las Fechas
    datos_max = dict(
		    zip(self.grados_fahrenheit,
		        self.fecha))  #Variable que nos permite tener un diccionario auxiliar más efectivo
		
    maxima_fecha =max(
		    datos_max.items(), key=lambda x: x[1]
		) 
    #items Devuelve una lista de tuplas
		#Key Mostrara los datos del diccionario
		#lambda función anónima dentro de otra función
	
    modificar = open("temperaturas.txt",
		             "a")  #Abrira el Archivo y modificara gracias a la variable a = append
    modificar.write("Las Fechas que Ingreso son= " + str(datos_max)+"\n") #Variable que permite 
   
    modificar.write("La Temperatura Maxima que Ingreso Converida en grados Fahrenheit es de= " + str(maxima_fecha))  #Imprimira resultado de la temperatura Maxima
    modificar.close()  #Cierra el Archivo Editado
    print("La Temperatura Maxima que Ingreso Convertida en Grados Fahrenheit es= " + str(maxima_fecha))  #imprime La temperatura Maxima & Su FECHA 

  def promedio(self):
    self.promedio_total = sum(
		    self.grados_centigrados) / contador  
		
    self.promedio_total_fahrenheit = sum(
		    self.grados_fahrenheit) / contador  #calcula el promedio Total de los grados FAHRENHEIT
    print("El Promedio Total de los grados Fahrenheit es= " + str(self.promedio_total_fahrenheit) + "\n")
    print("El Promedio Total de los Centigrados es de= " + str(
		    self.promedio_total_fahrenheit) + "\n")  #Imprime el pormedio Total de los grados Fahrenheit

  def archivo_de_texto(self): #Metodo archivo de texto que Modificaremos
    modificar = open("temperaturas.txt",
		             "a")  #abre el archivo en modo append o agregar
    modificar.write("El Promedio Total de los grados centigrados es de= " + str(
		    self.promedio_total) + "\n")  #Agregara en el Archivo el Total de los grados Centigrados
    modificar.write("El promedio Total de grados Fahrenheit es de= " + str(
		    self.promedio_total_fahrenheit) + "\n")  #Agregara en el Archivo el Total de los grados Fahrenheit
    modificar.close()# Variable que permite cerrar el archivo Editado


objeto = Temperaturas()  #declaramos el objeto del Metodo Temperaturas

r = "S"  #variable respuesta se S = continuar
while r == "S" or r == "s":  #Mientras respuesta sea S vs S el programa seguira su curso 
	contador += 1  #El contador  decclarado al Principio sumara +1 y asi a su vez cada que Ingresemos Un dato
	objeto.FechasTemperaturas()  #Objeto del Metodo FechasTemperaturas
	r = input("¿Desea Ingresar otra Temperatura Y Fecha? s/n "
	                  )  #
	if r == "N" or r == "n":  #si la respuesta es n vs N
		objeto = Temperaturas()  #se declara el objeto Temperaturas
		objeto.promedio()  #Objeto del Metodo Promedio
		objeto.ConvierteyBusca()  #Objeto del Metodo ConvertiryBuscar
		objeto.archivo_de_texto()  #Objeto metodo archivo_de_Texto
		break  #Finaliza el Programa


    