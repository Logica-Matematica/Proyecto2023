import random
def PiedraPapelTijera(nickname1, nickname2):
    jugador1 = ""
    jugador2 = ""
    piedra = "piedra"
    papel = "papel"
    tijera = "tijera"
    ganador1 = "jugador 1"
    ganador2 = "jugador 2"
    ganador3 = "jugador 3"
    x = random.randint(1, 3)
    if x == 1:
        print("El jugador 1 eligió papel")
        jugador1 = papel
    elif x == 2:
        print("El jugador 1 eligió piedra")
        jugador1 = piedra
    else:
        print("El jugador 1 eligió tijera")
        jugador1 = tijera
    z = random.randint(1, 3)
    if z == 1:
        print("El jugador 2 eligió papel")
        jugador2 = papel
    elif z == 2:
        print("El jugador 2 eligió piedra")
        jugador2 = piedra
    else:
        print("El jugador 2 eligió tijera")
        jugador2 = tijera
    if jugador1 == jugador2:
        resultado = 1
    elif jugador1 == papel and jugador2 == tijera or jugador1 == piedra and jugador2 == papel or jugador1 == tijera and jugador2 == piedra:
        resultado = 2
    else:
        resultado = 3
    if resultado == 1:
        print("Resultado de la primera ronda es empate")
    elif resultado == 2:
        print("Resultado de la primera ronda es ganador " + ganador2)
    else:
        print("Resultado de la primera ronda es ganador " + ganador3)
    x = random.randint(1, 3)
    if x == 1:
        print("El jugador 1 eligió papel")
        jugador1 = papel
    elif x == 2:
        print("El jugador 1 eligió piedra")
        jugador1 = piedra
    else:
        print("El jugador 1 eligió tijera")
        jugador1 = tijera
    z = random.randint(1, 3)
    if z == 1:
        print("El jugador 2 eligió papel")
        jugador2 = papel
    elif z == 2:
        print("El jugador 2 eligió piedra")
        jugador2 = piedra
    else:
        print("El jugador 2 eligió tijera")
        jugador2 = tijera
    if jugador1 == jugador2:
        resultado = 1
    elif jugador1 == papel and jugador2 == tijera or jugador1 == piedra and jugador2 == papel or jugador1 == tijera and jugador2 == piedra:
        resultado = 2
    else:
        resultado = 3
    if resultado == 1:
        print("Resultado de la segunda ronda es empate")
    elif resultado == 2:
        print("Resultado de la segunda ronda es ganador " + ganador2)
    else:
        print("Resultado de la segunda ronda es ganador " + ganador3)
    x = random.randint(1, 3)
    if x == 1:
        print("El jugador 1 eligió papel")
        jugador1 = papel
    elif x == 2:
        print("El jugador 1 eligió piedra")
        jugador1 = piedra
    else:
        print("El jugador 1 eligió tijera")
        jugador1 = tijera
    z = random.randint(1, 3)
    if z == 1:
        print("El jugador 2 eligió papel")
        jugador2 = papel
    elif z == 2:
        print("El jugador 2 eligió piedra")
        jugador2 = piedra
    else:
        print("El jugador 2 eligió tijera")
        jugador2 = tijera
    if jugador1 == jugador2:
        resultado = 1
    elif jugador1 == papel and jugador2 == tijera or jugador1 == piedra and jugador2 == papel or jugador1 == tijera and jugador2 == piedra:
        resultado = 2
    else:
        resultado = 3
    if resultado == 1:
        print("Resultado de la tercera ronda es empate")
    elif resultado == 2:
        print("Resultado de la tercera ronda es ganador " + ganador2)
    else:
        print("Resultado de la tercera ronda es ganador " + ganador3)
    
    print("Jose Daniel Choque Apaza")
#Jorge Cabrera

def JuegoDeLosDados(nickname1, nickname2):
    print("Bienvenidos al juego de los dados")
    
    print("Primera Ronda")
    Dado1 = random.randint(1, 6)
    Dado2 = random.randint(1, 6)
    print("El jugador", nickname1, "obtuvo", Dado1)
    print("El jugador", nickname2, "obtuvo", Dado2)
    if Dado1 == Dado2:
        Ganador1 = nickname1
    else:
        Ganador1 = nickname2
    print("El ganador de la primera ronda es", Ganador1)
    
    print("Segunda Ronda")
    Dado3 = random.randint(1, 6)
    Dado4 = random.randint(1, 6)
    print("El jugador", nickname1, "obtuvo", Dado3)
    print("El jugador", nickname2, "obtuvo", Dado4)
    if Dado3 == Dado4:
        Ganador2 = nickname1
    else:
        Ganador2 = nickname2
    print("El ganador de la segunda ronda es", Ganador2)
    
    print("Tercera Ronda")
    Dado5 = random.randint(1, 6)
    Dado6 = random.randint(1, 6)
    print("El jugador", nickname1, "obtuvo", Dado5)
    print("El jugador", nickname2, "obtuvo", Dado6)
    if Dado5 == Dado6:
        Ganador3 = nickname1
    else:
        Ganador3 = nickname2
    print("El ganador de la tercera ronda es", Ganador3)
    
    if Ganador1 == nickname1 and Ganador2 == nickname1 and Ganador3 == nickname1:
        ganadorDefinitivo = nickname1
    elif Ganador1 == nickname1 and Ganador2 == nickname1 and Ganador3 == nickname2:
        ganadorDefinitivo = nickname1
    elif Ganador1 == nickname1 and Ganador2 == nickname2 and Ganador3 == nickname1:
        ganadorDefinitivo = nickname1
    elif Ganador1 == nickname2 and Ganador2 == nickname1 and Ganador3 == nickname1:
        ganadorDefinitivo = nickname1
    elif Ganador1 == nickname2 and Ganador2 == nickname2 and Ganador3 == nickname2:
        ganadorDefinitivo = nickname2
    elif Ganador1 == nickname2 and Ganador2 == nickname2 and Ganador3 == nickname1:
        ganadorDefinitivo = nickname2
    elif Ganador1 == nickname2 and Ganador2 == nickname1 and Ganador3 == nickname2:
        ganadorDefinitivo = nickname2
    elif Ganador1 == nickname1 and Ganador2 == nickname2 and Ganador3 == nickname2:
        ganadorDefinitivo = nickname2
    print("El ganador del juego es", ganadorDefinitivo)
#NumeroDelMedio Oscar Mancilla Canaviri

def aleatory():
    numeroAleatorio=random.randint(100,999)
    aleatorioEnCaracter=str(numeroAleatorio)
    digitoDelMedio=int(aleatorioEnCaracter[1:2])
    return digitoDelMedio

def Ronda(nickname1,nickname2):
    digitoDelMedio=aleatory()
    respuesta1=int(input("intenta adivinar el numero del medio del numero aleatorio :"))
    if respuesta1==digitoDelMedio:
        print("Felicidades " + nickname1 + " acertaste")
    else:
        respuesta1=int(input("incorrecto te quedan 2 intentos :D "))
        if respuesta1==digitoDelMedio:
            print("Felicidades " + nickname1 + " acertaste")
            acertadaJugador1=1
        else:
            respuesta1=int(input("incorrecto te quedan 1 intento :D "))
            if respuesta1==digitoDelMedio:
                print("Felicidades " + nickname1 + " acertaste")
                acertadaJugador1=1
            else:
                print("\nEl numero era ", digitoDelMedio)
                acertadaJugador1=0
    return acertadaJugador1

def Rondaa(nickname1,nickname2):
    digitoDelMedio=aleatory()
    print("\nturno de " + nickname2)
    respuesta2=input("intenta adivinar el numero del medio del numero aleatorio :")
    if respuesta2==digitoDelMedio:
        print("Felicidades " + nickname2 + " acertaste")
        acertadaJugador2=1
    else:
        respuesta2=int(input("incorrecto te quedan 2 intentos :D  "))
        if respuesta2==digitoDelMedio:
            print("Felicidades " + nickname2 + " acertaste")
            acertadaJugador2=1
        else:
            respuesta2=int(input("incorrecto te quedan 1 intento :D "))
            if respuesta2==digitoDelMedio:
                print("Felicidades " + nickname2 + " acertaste")
                acertadaJugador2=1
            else:
                acertadaJugador2=0
                print("\nEl numero era ", digitoDelMedio)
    return acertadaJugador2

def impresionDeResultado(acertadaJugador1,acertadaJugador2,nickname1,nickname2):
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    if acertadaJugador2==acertadaJugador1:
        print( "Esto es un empate")
    elif acertadaJugador2<acertadaJugador1:
        print("Gano " + nickname1)
    elif acertadaJugador2>acertadaJugador1:
        print("Gano " + nickname2)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

def NumeroDelMedio(nickname1, nickname2):
    print("PRIMERA RONDA")
    acertadaJugador1=Ronda(nickname1,nickname2)
    acertadaJugador2=Rondaa(nickname1,nickname2)
    impresionDeResultado(acertadaJugador1,acertadaJugador2,nickname1,nickname2)
    rondaJugador1ronda1=acertadaJugador1
    rondaJugador2ronda1=acertadaJugador2
    
    print("SEGUNDA RONDA")
    acertadaJugador1=Ronda(nickname1,nickname2)
    acertadaJugador2=Rondaa(nickname1,nickname2)
    impresionDeResultado(acertadaJugador1,acertadaJugador2,nickname1,nickname2)
    
    rondaJugador1ronda2=acertadaJugador1
    rondaJugador2ronda2=acertadaJugador2
    
    print("TERCERA RONDA")
    acertadaJugador1=Ronda(nickname1,nickname2)
    acertadaJugador2=Rondaa(nickname1,nickname2)
    impresionDeResultado(acertadaJugador1,acertadaJugador2,nickname1,nickname2)
    
    rondaJugador1ronda3=acertadaJugador1
    rondaJugador2ronda3=acertadaJugador2
    
    rondasGanadasJugador1=rondaJugador1ronda1+rondaJugador1ronda2+rondaJugador1ronda3
    rondasGanadasJugador2=rondaJugador2ronda1+rondaJugador2ronda2+rondaJugador2ronda3
    if rondasGanadasJugador1>rondasGanadasJugador2:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("FELICIDADES " + nickname1 + " GANASTE")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    elif rondasGanadasJugador1<rondasGanadasJugador2:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("FELICIDADES " + nickname2 + " GANASTE")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#NumeroDelMedio Oscar Mancilla Canaviri


def calculo():
    nick = str(random.randint(10, 99))
    name = input("Ingrese el nombre del jugador 1: ")
    tresCaracteres = name[:3]
    nickname1 = tresCaracteres + nick
    print("El nickname del jugador 1 sera: ", nickname1)
    return nickname1

def calculo2():
    nick2 = str(random.randint(10, 99))
    name2 = input("Ingrese el nombre del jugador 2: ")
    tresCaracteres = name2[:3]
    nickname2 = tresCaracteres + nick2
    print("El nickname del jugador 2 sera: ", nickname2)
    return nickname2

def juegosMultiples():
    nickname1 = calculo()
    nickname2 = calculo2()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%") 
    print("Por favor seleccione un juego")
    print("1.- Piedra papel o tijeras")
    print("2.- Dados")
    print("3.- Numero del medio")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    respuesta = input()
    if respuesta == "1":
        PiedraPapelTijera(nickname1, nickname2)
    elif respuesta == "2":
        JuegoDeLosDados(nickname1, nickname2)
    elif respuesta == "3":
        NumeroDelMedio(nickname1, nickname2)
    else:
        print("opcion invalida")
        

juegosMultiples()
