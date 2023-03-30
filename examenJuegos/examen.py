def aleatory():
    numeroAleatorio=random.randint(100,999)
    aleatorioEnCaracter=str(numeroAleatorio)
    digitoDelMedio=int(aleatorioEnCaracter[1:2])
    return digitoDelMedio

def Ronda(respuesta1,digitoDelMedio):
    if respuesta1==digitoDelMedio:
        print("Felicidades acertaste")
        acertadaJugador1=1
    else:
        respuesta1=int(input("incorrecto te quedan 2 intentos :D  "))
        if respuesta1==digitoDelMedio:
            print("Felicidades acertaste")
            acertadaJugador1=1
        else:
            respuesta1=int(input("incorrecto te quedan 1 intento :D"))
            if respuesta1==digitoDelMedio:
                print("Felicidades acertaste")
                acertadaJugador1=1
            else:
                acertadaJugador1=0
    return acertadaJugador1

def Ronda(respuesta2,digitoDelMedio):
    if respuesta2==digitoDelMedio:
        print("Felicidades acertaste")
        acertadaJugador2=1
    else:
        respuesta2=int(input("incorrecto te quedan 2 intentos :D  "))
        if respuesta2==digitoDelMedio:
            print("Felicidades acertaste")
            acertadaJugador2=1
        else:
            respuesta2=int(input("incorrecto te quedan 1 intento :D"))
            if respuesta2==digitoDelMedio:
                print("Felicidades acertaste")
                acertadaJugador2=1
            else:
                acertadaJugador2=0
    return acertadaJugador2

    
import random
digitoDelMedio=aleatory()
respuesta1=input("intenta adivinar el numero del medio del numero aleatorio :")
acertadaJugador1=Ronda(respuesta1,digitoDelMedio)
digitoDelMedio=aleatory()
print("turno del jugador 2")
respuesta2=input("intenta adivinar el numero del medio del numero aleatorio :")
acertadaJugador2=Ronda(respuesta2,digitoDelMedio)
print("segunda Ronda")
acertadaJugador1ronda2=Ronda(respuesta1,digitoDelMedio)
print("turno del jugador 2")
respuesta2=input("intenta adivinar el numero del medio del numero aleatorio :")
acertadaJugador2ronda2=Ronda(respuesta2,digitoDelMedio)
print("tercera ronda")
acertadaJugador1ronda3=Ronda(respuesta1,digitoDelMedio)
print("turno del jugador 2")
respuesta2=input("intenta adivinar el numero del medio del numero aleatorio :")
acertadaJugador2ronda3=Ronda(respuesta2,digitoDelMedio)


