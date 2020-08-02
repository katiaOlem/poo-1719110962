r="S" #variable que ayudara al ciclo while
datos_peli=[]
genero=[] #arreglo para almacenar el genero de la pelicula
peliculas=[]
class Peliculas: #creamos la clase Peliculas
  def __init__(self): #definimos el metodo contructor
        pass
  def DatosPeliculas(self): #metodo que pide los datos de las peliculas
      
      nombre=input("Nombre de la pelicula: ") #pide el nombre de la pelicula
      anio=input("Año de lanzamiento: ") #pide el año de lanzamiento de la pelicula
      genero_pelicula=input("Genero de la pelicula: ") #pide el genero de la pelicula

      datos_peli.append(nombre, anio)
      genero.append(genero_pelicula) 
      diccionario={"Nombre":nombre,"Año de Lanazamiento":anio,"Genero":genero_pelicula}
      peliculas.append(diccionario)


      print(peliculas) #imprime el diccionario creado
    

      nombre_genero=input("Genero de la Pelicula que desea= ") #pide el nombre de un genero de pelicula
      if nombre_genero in diccionario.values(): #si el nombre del genero esta el los valores del diccionario
            for catalogo in diccionario: #lee el diccionario
                if peliculas[catalogo]==nombre_genero: #si el diccionario tiene el genero que insertaste
                    print(catalogo) #impime las peliculas con ese genero
 
while r=="s" or r=="S": #mientras respuesta sea S o s
    objeto_Peliculas=Peliculas() #Llama a la clase objeto
    objeto_Peliculas.DatosPeliculas() #invoca a los el metodo que pide los datos
    r=input("¿Desea Capturar mas peliculas? S/N ") #si deseas continuar capturando peliculas 
    if r=="n" or r=="N": #si la respuesta es n o N
        
        break #finaliza el codigo con un brake
        
                
  
    
        