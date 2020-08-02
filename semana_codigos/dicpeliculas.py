r="S" #variable de respuesta
datos_pelicula=[] #Contador de las variables nombre y año de la pelicula
generos=[] #Contador de los generos

class Peliculas: #Clase
    def __init__(self): #Metodo contructor
        pass
    def DatosPeliculas(self): #Metodo de las Peliculas 
      
       nombre=input("Nombre Pelicula  ") #Variable del nombre de la pelicula
       anio=input("Año de su Lanzamiento  ") #Variable del año en que se lanzo la Pelicula
       genero_pelicula=input("Genero  ") #Variable del genero de la pelicula
       datos_pelicula.append("Pelicula  " + str (nombre)+ "Año  "+ str (anio)) #Reemplazar y guardar los Datos de nombre y anio de la Pelicula en el contador datos_pelicula
       generos.append("Genero  "+ str(genero_pelicula)) #Reemplazaremos y guardaremos los generos_peliculas en el contador gneros

    def DiccionarioPeliculas(self): #Metodo DiccionarioPeliculas

        datos_peli=dict(zip(datos_pelicula,generos)) #Diccionario con el comando dict y zip para obtener un diccionario de nuestros datos pelicula y generos
      

        print(datos_peli) #Imprimir el Diccionario con nuestros datos
      

        generos_list=input("Genero de la Pelicula que desea ver  ") #pide el nombre de un genero de pelicula

        if generos_list in datos_peli.keys():  #Condicion de que si el genero_lista esta en el diccionario keys retorna el diccionario de los datos
           for lista in datos_peli: #Encontrara los generos
               if datos_peli[lista] == generos_list: #los leera
                  print("Las peliculas Disponibles son=" + str (lista))#Lo imprime con las Peliculas de ese genero
while r=="s" or r=="S":  #Condicion para repetir el Programa Creado si la respuesta es si  Leera los Datos de la pelicula e Imprimira.
    obj=Peliculas()
    obj.DatosPeliculas() 
#Si la respuesta es no solo imprimira la lista de las peliculas con los generos que desee 
    r=input(" \n ¿Desea Ingresar otra Pelicula? s/n ") 
    if r=="n" or r=="N": 
        obj.DiccionarioPeliculas()
        break 
        
                
  
    
        