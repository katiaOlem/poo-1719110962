r="S" #variable que ayudara al ciclo while
datos_pelicula=[]
generos=[]

class Peliculas: #creamos la clase Peliculas
    def __init__(self): #definimos el metodo contructor
        pass
    def DatosPeliculas(self): #metodo que pide los datos de las peliculas
      
       nombre=input("Nombre Pelicula  ") #pide el nombre de la pelicula
       anio=input("Año de su Lanzamiento  ") #pide el año de lanzamiento de la pelicula
       genero_pelicula=input("Genero  ") #pide el genero de la pelicula
       datos_pelicula.append("Pelicula  " + str (nombre)+ "Año  "+ str (anio))
       generos.append("Genero  "+ str(genero_pelicula))

    def DiccionarioPeliculas(self):

        datos_peli=dict(zip(datos_pelicula,generos))
      

        print(datos_peli)
      

        generos_list=input("Genero de la Pelicula que desea ver  ") #pide el nombre de un genero de pelicula

        if generos_list in datos_peli.keys(): 
           for lista in datos_peli: #lee el diccionario
               if datos_peli[lista] == generos_list: #si el diccionario tiene el genero que insertaste
                  print("Las peliculas Disponibles son=" + str (lista))#impime las peliculas con ese genero
while r=="s" or r=="S": 
    obj=Peliculas()
    obj.DatosPeliculas() 

    r=input(" \n ¿Desea Ingresar otra Pelicula? s/n ") 
    if r=="n" or r=="N": 
        obj.DiccionarioPeliculas()
        break 
        
                
  
    
        