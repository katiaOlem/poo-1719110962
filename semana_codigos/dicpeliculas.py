r="S" #variable de respuesta
anio_pelicula=[] #varible que nos permite almacenar el año de la pelicula
genero=[] #varible que nos permite almacenar los generos
nombre_pelicula=[] # Variable que nospermite almacenar el nombre de la pelicula
class Peliculas: #clase Peliculas
    def __init__(self): #Metodo contructor
        pass
    def DatosPeli(self): #Metodode los Datos de la Pelicula
        nombre=input("Ingrese el Nombre de la pelicula= ") #Variable que nos permite ingresar el nombre de la Pelicula
        anio=input("Ingrese Año de lanzamiento de la Pelicula= ") #Variable que nos permite ingresar el año de lanzamiento de la pelicula
        genero_peli=input("Ingrese el Genero de la pelicula= ") #Variable que nos permite ingresar el genero de la Pelicula
        nombre_pelicula.append("El nombre de la Pelicula es ="+str (nombre))

        anio_pelicula.append("EL Año de la Pelicula es= " +str(anio)) #agrega la variable anio_pelicula el año

        genero.append("EL genero de la Peliculla es="+ str (genero_peli)) #añade el nombre del genero de la pelicula
    def DiccionarioPeliculas(self): #metodo que ayudara a que el diccionario busque e Imprima
        peliculas=dict(zip(nombre_pelicula,anio_pelicula,genero)) #Nos permitira que dict haga un diccionario con las variables obtenidas
        print(peliculas) #Imprimira el arreglo

        generos=input("Ingrese el Genero de la pelicula: ") #Variable en la que se ingresara los generos
        if generos in datos.values(): #si el nombre del genero esta el los valores del diccionario
            for catalogo in peliculas: #lee el diccionario
                if peliculas[catalogo]==generos: #si el diccionario tiene el genero que insertaste
                    print(catalogo) #impime las peliculas con ese genero
while r=="s" or r=="S": #mientras respuesta sea S o s
    objeto_Peliculas=Peliculas ()
    objeto_Peliculas.DatosPeli ()
    r=input("¿Desea Leer mas peliculas? s/n ") #si deseas continuar capturando peliculas 
    if r=="n" or r=="N": #si la respuesta es n o N
        objeto_Peliculas.DiccionarioPeliculas () #invoca al metodo de que busca y crea un diccionario
        break #finaliza el codigo con un brake
        