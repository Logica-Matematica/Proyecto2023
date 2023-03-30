import random
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
        acertadaJugador1=1
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





#NumeroDelMedio            Oscar Mancilla Canaviri
print("PRIMERA RONDA")
nickname1=input()
nickname2=input()
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

