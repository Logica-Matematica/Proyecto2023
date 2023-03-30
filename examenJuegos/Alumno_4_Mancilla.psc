Algoritmo Alumno_4_Mancilla
	numeroAleatorio=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	Imprimir digitoDelMedio
	Escribir " intenta adivinar el numero del medio del numero aleatorio"
	Leer respuesta1
	Si respuesta1=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste"
		acertadaJugador1=1
		
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta1
		Si respuesta1=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste"
			acertadaJugador1=1
			
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta1
			
			Si respuesta1=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste"
				acertadaJugador1=1
			SiNo
				acertadaJugador1=0
			Fin Si
		Fin Si
	Fin Si
	
	numeroAleatorio2=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio2)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	imprimir digitoDelMedio
	Escribir "Turno Del jugador2"
	leer respuesta2
	Si respuesta2=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste"
		acertadaJugador2=1
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta2
		
		Si respuesta2=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste"
			acertadaJugador2=1
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta2
			
			Si respuesta2=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste"
				acertadaJugador2=1
			SiNo
				acertadaJugador2=0
			Fin Si
		Fin Si
	Fin Si
	
	
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	Imprimir "Ronda1"
	Si acertadaJugador2=acertadaJugador1 Entonces
		Imprimir "Esto es un empate"
		rondaJugador1ronda1=0
		rondaJugador2ronda1=0
	SiNo
		Si acertadaJugador2<acertadaJugador1 Entonces
			Imprimir "el jugador 1 ganooo"
			rondaJugador1ronda1=1
			rondaJugador2ronda1=0
		SiNo
			Si acertadaJugador2>acertadaJugador1 Entonces
				Imprimir "el jugador 2 ganooo"
				rondaJugador2ronda1=1
				rondaJugador1ronda1=0
			Fin Si
		Fin Si
	Fin Si
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	Esperar 2 Segundos
	Imprimir ""
	Imprimir "Ronda 2"
	Esperar 1 Segundos
	numeroAleatorio=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	Imprimir digitoDelMedio
	Escribir " intenta adivinar el numero del medio del numero aleatorio"
	Leer respuesta1
	Si respuesta1=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste"
		acertadaJugador1=1
		
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta1
		Si respuesta1=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste"
			acertadaJugador1=1
			
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta1
			
			Si respuesta1=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste"
				acertadaJugador1=1
			SiNo
				acertadaJugador1=0
			Fin Si
		Fin Si
	Fin Si
	
	numeroAleatorio2=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio2)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	imprimir digitoDelMedio
	Escribir "Turno Del jugador2"
	leer respuesta2
	Si respuesta2=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste"
		acertadaJugador2=1
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta2
		
		Si respuesta2=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste"
			acertadaJugador2=1
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta2
			
			Si respuesta2=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste"
				acertadaJugador2=1
			SiNo
				acertadaJugador2=0
			Fin Si
		Fin Si
	Fin Si
	
	
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	Imprimir "Ronda2"
	Si acertadaJugador2=acertadaJugador1 Entonces
		Imprimir "Esto es un empate"
		rondaJugador1ronda2=0
		rondaJugador2ronda2=0
	SiNo
		Si acertadaJugador2<acertadaJugador1 Entonces
			Imprimir "el jugador 1 ganooo"
			rondaJugador1ronda2=1
			rondaJugador2ronda2=0
		SiNo
			Si acertadaJugador2>acertadaJugador1 Entonces
				Imprimir "el jugador 2 ganooo"
				rondaJugador2ronda2=1
				rondaJugador1ronda2=0
			Fin Si
		Fin Si
	Fin Si
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	
	Esperar 2 Segundos
	Imprimir ""
	Imprimir "Ronda 3"
	Esperar 1 Segundos
	numeroAleatorio=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	Imprimir digitoDelMedio
	Escribir " intenta adivinar el numero del medio del numero aleatorio"
	Leer respuesta1
	Si respuesta1=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste"
		acertadaJugador1=1
		
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta1
		Si respuesta1=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste"
			acertadaJugador1=1
			
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta1
			
			Si respuesta1=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste"
				acertadaJugador1=1
			SiNo
				acertadaJugador1=0
			Fin Si
		Fin Si
	Fin Si
	
	numeroAleatorio2=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio2)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	imprimir digitoDelMedio
	Escribir "Turno Del jugador2"
	leer respuesta2
	Si respuesta2=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste"
		acertadaJugador2=1
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta2
		
		Si respuesta2=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste"
			acertadaJugador2=1
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta2
			
			Si respuesta2=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste"
				acertadaJugador2=1
			SiNo
				acertadaJugador2=0
			Fin Si
		Fin Si
	Fin Si
	
	
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	Imprimir "Ronda3"
	Si acertadaJugador2=acertadaJugador1 Entonces
		Imprimir "Esto es un empate"
		rondaJugador1ronda3=0
		rondaJugador2ronda3=0
	SiNo
		Si acertadaJugador2<acertadaJugador1 Entonces
			Imprimir "el jugador 1 ganooo"
			rondaJugador1ronda3=1
			rondaJugador2ronda3=0
		SiNo
			Si acertadaJugador2>acertadaJugador1 Entonces
				Imprimir "el jugador 2 ganooo"
				rondaJugador2ronda3=1
				rondaJugador1ronda3=0
			Fin Si
		Fin Si
	Fin Si
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	
	rondasGanadasJugador1=rondaJugador1ronda1+rondaJugador1ronda2+rondaJugador1ronda3
	rondasGanadasJugador2=rondaJugador2ronda1+rondaJugador2ronda2+rondaJugador2ronda3
	Imprimir rondasGanadasJugador1
	Imprimir rondasGanadasJugador2
	Si rondasGanadasJugador1>rondasGanadasJugador2 Entonces
		Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
		Imprimir "FELICIDADES JUGADOR 1 GANASTE"
		Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	SiNo
		Si rondasGanadasJugador1<rondasGanadasJugador2 Entonces
			Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
			Imprimir "FELICIDADES JUGADOR 2 GANASTE"
			Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
		FinSi
	FinSi
	
FinAlgoritmo
