class CodigoCesar: #CLASE
    def __init(self): #CONSTRUCTOR
        pass
    def cifradoDesifrado(self): 
        respuesta="S" #VARIBLE
        while respuesta=="S" or respuesta=="s": # Funciona para volver a cifrar o decifrar el texto
            cifrado = [] #variable del cifrado
            decifrar = []  #variable del decifrado
            condicion=input("Desea Cifrar o Decifrar una cadena? ") #tomar la decision de que desea hacer  nuevamente 
            if condicion=="cifrar" or condicion=="Cifrar": 
                cadena=input("Inserta la cadena a cifrar ") #pide la cadena que se quiere cifrar
                cadena_a_cifrar=cadena.lower() #convierte la cadena  a minisculas
                for convertir in cadena_a_cifrar: 
                    cifrado.append(ord(convertir)) # ASCII 
                print(cifrado) #Imprime la cadena cifrada
                respuesta = input("¿Desea Cifrar/Descifrar otra cadena s/n?")  # pregunta si quiere repetir el proceso en cifrar o desifrar 
                if respuesta == "N" or respuesta == "n":  # Si la respuesta es N Vs n termina 
                    break
            if pregunta=="Decifrar" or pregunta=="decifrar": #condicion
                cadena=input("Inserte cadena a decifrar ") #pide la cadena que se desea desifrar
                decifrar_cadena=tuple(map(str,cadena.split(","))) #Cadena arreglada 
                for decifrado in decifrar_cadena:#
                                        decifrar.append(enie)

                    f decifrado in "97,":
                        a=chr(97) #convierte el numero a letra
                        decifrar.append(a) #la almacena en la variable decifrar de tipo tupla o arreglo
                    elif decifrado in "98,":
                        b=chr(98)
                        decifrar.append(b)
                    elif decifrado in "99,":
                        c=chr(99)
                        decifrar.append(c)
                    elif decifrado in "100,":
                        d=chr(100)
                        decifrar.append(d)
                    elif decifrado in "101,":
                        e=chr(101)
                        decifrar.append(e)
                    elif decifrado in "102,":
                        f=chr(102)
                        decifrar.append(f)
                    elif decifrado in "103,":
                        g=chr(103)
                        decifrar.append(g)
                    elif decifrado in "104,":
                        h=chr(104)
                        decifrar.append(h)
                    elif decifrado in "105,":
                        i=chr(105)
                        decifrar.append(i)
                    elif decifrado in "106":
                        j=chr(106)
                        decifrar.append(j)
                    elif decifrado in "107,":
                        k=chr(107)
                        decifrar.append(k)
                    elif decifrado in "108,":
                        l=chr(108)
                        decifrar.append(l)
                    elif decifrado in "109,":
                        m=chr(109)
                        decifrar.append(m)
                    elif decifrado in "110,":
                        n=chr(110)
                        decifrar.append(n)
                    elif decifrado in "111,":
                        o=chr(111)
                        decifrar.append(o)
                    elif decifrado in "112,":
                        p=chr(112)
                        decifrar.append(p)
                    elif decifrado in "113,":
                        q=chr(1113)
                        decifrar.append(q)
                    elif decifrado in "114,":
                        r=chr(114)
                        decifrar.append(r)
                    elif decifrado in "115,":
                        s=chr(115)
                        decifrar.append(s)
                    elif decifrado in "116,":
                        t=chr(116)
                        decifrar.append(t)
                    elif decifrado in "117,":
                        u=chr(117)
                        decifrar.append(u)
                    elif decifrado in "118,":
                        v=chr(118)
                        decifrar.append(v)
                    elif decifrado in "119,":
                        w=chr(119)
                        decifrar.append(w)
                    elif decifrado in "120,":
                        x=chr(120)
                        decifrar.append(x)
                    elif decifrado in "121,":
                        y=chr(121)
                        decifrar.append(y)
                    elif decifrado in "122,":
                        z=chr(122)
                        decifrar.append(z)
                    elif decifrado in "164,":
                        enie=chr(164)
                    elif decifrado in "32,":
                        espacio=chr(32)
                        decifrar.append(espacio)

                print(decifrar) #impirme la cadena decifrada
                respuesta=input("¿Desea cifrar/descifrar otra cadena s/n?") #Permite repetiir el proceso
                if respuesta=="N" or respuesta=="n": #Si la respuesta es N vs n
                    break #finaliza 
objeto_codigo=CodigoCesar() 
objeto_codigo.cifradoDesifrado() 