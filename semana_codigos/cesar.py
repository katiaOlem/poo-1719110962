class CodigoCesar: #Clase
    def __init__(self): #Metodo constructor
        pass
    def CifradoDesifrado(self): #Metodo
       r="S"
       while r=="S" or r=="s": #Opcion de S continua
            cifrado = [] # alamacena la cadena cifrada
            descifrar = []  #almacena la cadena desifrada
            pregunta=input("Desea Cifrar o Descifrar una Cadena? ") #Da la Opcion de Cifrar o Descifrar
            if pregunta=="cifrar" or pregunta=="Cifrar": #Respuesta de Cifrar hará el proceso 
                cadena=input("Inserta la cadena a cifrar ") 
                cadena_cifrar=cadena.lower() #Toda la cadena pasa a Minusculas en caso de que este en Mayusculas
                for convertir in cadena_cifrar: 
                    cifrado.append(ord(convertir))
                     #convierte toda la cadena en un numero ASCII
                print("La cadena cifrada es = "+str(cifrado)) #Imprime la cadena Cifrada
                r = input("¿Desea cifrar/descifrar otra cadena s/n?")  # pregunta si quiere repetir el proceso
                if r == "N" or r == "n":  # Si la respuesta es "N" vs "n"
                    break #Finaliza
            if pregunta=="Descifrar" or pregunta=="descifrar": #Respuesta de descifrar para comenzar el proceso
                cadena=input("Inserta tu cadena a descifrar ") 
                descifrar_cadena=tuple(map(str,cadena.split(","))) #Manera de hacer mas sensillo y elegante  el proceso de las Tuplas
                for descifrado in descifrar_cadena:
          # Remplazaremos las letras y los numeros por numeros para que descifrar la cadena
                    if descifrado in "97,":
                        a=chr(97) 
                        descifrar.append(a) 
                    elif descifrado in "98,":
                        b=chr(98)
                        descifrar.append(b)
                    if descifrado in "99,":
                        c=chr(99)
                        descifrar.append(c)
                    elif descifrado in "100,":
                        d=chr(100)
                        descifrar.append(d)
                    if descifrado in "101,":
                        e=chr(101)
                        descifrar.append(e)
                    elif descifrado in "102,":
                        f=chr(102)
                        descifrar.append(f)
                    if descifrado in "103,":
                        g=chr(103)
                        descifrar.append(g)
                    elif descifrado in "104,":
                        h=chr(104)
                        descifrar.append(h)
                    if descifrado in "105,":
                        i=chr(105)
                        descifrar.append(i)
                    elif descifrado in "106":
                        j=chr(106)
                        descifrar.append(j)
                    if descifrado in "107,":
                        k=chr(107)
                        descifrar.append(k)
                    elif descifrado in "108,":
                        l=chr(108)
                        descifrar.append(l)
                    if descifrado in "109,":
                        m=chr(109)
                        descifrar.append(m)
                    elif descifrado in "110,":
                        n=chr(110)
                        descifrar.append(n)
                    if descifrado in "111,":
                        o=chr(111)
                        descifrar.append(o)
                    elif descifrado in "112,":
                        p=chr(112)
                        descifrar.append(p)
                    if descifrado in "113,":
                        q=chr(1113)
                        descifrar.append(q)
                    elif descifrado in "114,":
                        r=chr(114)
                        descifrar.append(r)
                    if descifrado in "115,":
                        s=chr(115)
                        descifrar.append(s)
                    elif descifrado in "116,":
                        t=chr(116)
                        descifrar.append(t)
                    if descifrado in "117,":
                        u=chr(117)
                        descifrar.append(u)
                    elif descifrado in "118,":
                        v=chr(118)
                        descifrar.append(v)
                    if descifrado in "119,":
                        w=chr(119)
                        descifrar.append(w)
                    elif descifrado in "120,":
                        x=chr(120)
                        descifrar.append(x)
                    if descifrado in "121,":
                        y=chr(121)
                        descifrar.append(y)
                    elif descifrado in "122,":
                        z=chr(122)
                        descifrar.append(z)
                    if descifrado in "164,":
                        enie=chr(164)
                        descifrar.append(enie)
                    elif descifrado in "32,":
                        espacio=chr(32)
                        descifrar.append(espacio)
                    if descifrado in "@,":
                        arroba=chr(64)
                        descifrar.append(arroba)
                    elif descifrado in "49,":
                        uno=chr(49)
                        descifrar.append(uno)
                    if descifrado in "50,":
                        dos=chr(50)
                        descifrar.append(dos)
                    elif descifrado in "51,":
                        tres=chr(51)
                        descifrar.append(tres)
                    if descifrado in "52,":
                        cuatro=chr(52)
                        descifrar.append(cuatro)
                    elif descifrado in "53,":
                        cinco=chr(53)
                        descifrar.append(cinco)
                    if descifrado in "54,":
                        seis=chr(54)
                        descifrar.append(seis)
                    elif descifrado in "55,":
                        siete=chr(55)
                        descifrar.append(siete)
                    if descifrado in "56,":
                        ocho=chr(56)
                        descifrar.append(ocho)
                    elif descifrado in "57,":
                        nueve=chr(57)
                        descifrar.append(nueve)
                    if descifrado in "48,":
                        cero=chr(48)
                        descifrar.append(cero)

                print("La cadena descifrada es = "+str(descifrar)) #Imprime la cadena Descifrada
                r=input("¿Desea cifrar/descifrar otra cadena s/n?") 
                if r=="N" or r=="n": 
                    break #FIN
#Objetos de la clase y metodo
objeto_codigo=CodigoCesar() 
objeto_codigo.CifradoDesifrado() 