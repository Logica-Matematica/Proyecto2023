Funcion acertadaJugador1=ronda(nickname1,nickname2) //OSCAR MANCILLA CANAVIRI
	numeroAleatorio=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	Escribir nickname1, " intenta adivinar el numero del medio del numero aleatorio"
	Leer respuesta1
	Si respuesta1=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste ", nickname1
		acertadaJugador=1
		
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta1
		Si respuesta1=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste ", nickname1
			acertadaJugador=1
			
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta1
			
			Si respuesta1=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste ", nickname1
				acertadaJugador=1
			SiNo
				Imprimir "perdiste todos tus intentos ", nickname1
				Imprimir "El numero era " digitoDelMedio
				acertadaJugador=0
				Esperar 1 Segundos
			Fin Si
		Fin Si
	Fin Si
	acertadaJugador1=0+acertadaJugador
FinFuncion

Funcion acertadaJugador2=rondaa(nickname1,nickname2)
	numeroAleatorio=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	Escribir "Turno De " nickname2
	leer respuesta2
	Si respuesta2=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste "
		acertadaJugador2=1
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta2
		
		Si respuesta2=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste "
			acertadaJugador2=1
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta2
			
			Si respuesta2=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste "
				acertadaJugador2=1
			SiNo
				Imprimir "perdiste todos tus intentos ", nickname2
				Imprimir "El numero era " digitoDelMedio
				acertadaJugador=0
				Esperar 1 Segundos
			Fin Si
		Fin Si
	Fin Si
FinFuncion


Funcion impresionDeResultado(acertadaJugador1,acertadaJugador2,nickname1,nickname2)
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	Si acertadaJugador2=acertadaJugador1 Entonces
		Imprimir "Esto es un empate"
	SiNo
		Si acertadaJugador2<acertadaJugador1 Entonces
			Imprimir "Gano " nickname1
		SiNo
			Si acertadaJugador2>acertadaJugador1 Entonces
				Imprimir "Gano " nickname2
			Fin Si
		Fin Si
	Fin Si
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
FinFuncion


funcion NumeroDelMedio(nickname1,nickname2)
	acertadaJugador1=ronda(nickname1,nickname2)
	acertadaJugador2=rondaa(nickname1,nickname2)
	rondaJugador1ronda1=acertadaJugador1
	rondaJugador2ronda1=acertadaJugador2
	Borrar Pantalla
	Imprimir "PRIMERA RONDA"
	impresionDeResultado(acertadaJugador1,acertadaJugador2,nickname1,nickname2)
	Esperar 2 Segundos
	
	Borrar Pantalla
	Imprimir "Ronda 2"
	acertadaJugador1=ronda(nickname1,nickname2)
	acertadaJugador2=rondaa(nickname1,nickname2)
	rondaJugador1ronda2=acertadaJugador1
	rondaJugador2ronda2=acertadaJugador2
	Borrar Pantalla
	Imprimir "SEGUNDA RONDA"
	impresionDeResultado(acertadaJugador1,acertadaJugador2,nickname1,nickname2)
	Esperar 2 Segundos
	Borrar Pantalla
	
	Imprimir "Ronda 3"
	acertadaJugador1=ronda(nickname1,nickname2)
	acertadaJugador2=rondaa(nickname1,nickname2)
	rondaJugador1ronda3=acertadaJugador1
	rondaJugador2ronda3=acertadaJugador2
	Borrar Pantalla
	Imprimir "TERCERA RONDA"
	impresionDeResultado(acertadaJugador1,acertadaJugador2,nickname1,nickname2)
	rondasGanadasJugador1=rondaJugador1ronda1+rondaJugador1ronda2+rondaJugador1ronda3
	rondasGanadasJugador2=rondaJugador2ronda1+rondaJugador2ronda2+rondaJugador2ronda3
	Si rondasGanadasJugador1>rondasGanadasJugador2 Entonces
		Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
		Imprimir "FELICIDADES " nickname1 " GANASTE"
		Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	SiNo
		Si rondasGanadasJugador1<rondasGanadasJugador2 Entonces
			Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
			Imprimir "FELICIDADES " nickname2 " GANASTE"
			Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
		FinSi
	FinSi
FinFuncion

Funcion nickname1= calculo()
	nick=ConvertirATexto(aleatorio(10,99))
	escribir "Ingrese el nombre del jugador 1"
	leer name
	tresCaracteres=Subcadena(name,1,3)
	nickname1=concatenar(tresCaracteres,nick)
	imprimir "El nickname del jugador 1 sera: ",nickname1
Fin Funcion

Funcion nickname2=calculo2()
	nick2=ConvertirATexto(aleatorio(10,99))
	escribir "Ingrese el nombre del jugador 2"
	leer name2
	tresCaracteres=Subcadena(name2,1,3)
	nickname2=concatenar(tresCaracteres,nick2)
	Imprimir "El nickname del jugador 2 sera: ",nickname2 
Fin Funcion





Algoritmo Alumno_4_Mancilla
	nickname1= calculo()
	nickname2=calculo2()
	NumeroDelMedio(nickname1,nickname2)
FinAlgoritmo










