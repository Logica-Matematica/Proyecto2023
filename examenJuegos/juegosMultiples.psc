Funcion  PiedraPapelTijera(nickname1,nickname2)
	//Alumno1 Daniel Choque
	
	X=Aleatorio(1,3)
	Si X=1 Entonces Escribir "El jugador 1 eligio papel"
	Sino si X=2 Escribir "El jugador 1 eligio piedra"
		SIno si X=3 Escribir "El jugador 1 eligio tijera"
				
			FinSi
		FinSi
	FinSi
	Z=Aleatorio(1,3)
	Si Z=1 Entonces Escribir "El jugador 2 eligio papel"
	Sino si Z=2 Escribir "El jugador 2 eligio piedra"
		SIno si Z=3 Escribir "El jugador 2 eligio tijera"
				
			FinSi
		FinSi
	FinSi
	Si X=Z Entonces
		resultado=1
	Sino si X=1 y Z=3 o X=2 y Z=1 o X=3 y Z=2
			resultado=2
			Si no resultado=3
			FinSi
		FinSi
	FinSi
	
	Segun resultado
		caso 1: Escribir "Resultado de la primera ronda es empate"
		caso 2: Escribir "Resultado de la primera ronda es ganador jugador 2"
		caso 3: Escribir "Resultado de la primera ronda es ganador jugador 3"
			
	fin segun 
	X=Aleatorio(1,3)
	Si X=1 Entonces Escribir "El jugador 1 eligio papel"
	Sino si X=2 Escribir "El jugador 1 eligio piedra"
		SIno si X=3 Escribir "El jugador 1 eligio tijera"
				
			FinSi
		FinSi
	FinSi
	Z=Aleatorio(1,3)
	Si Z=1 Entonces Escribir "El jugador 2 eligio papel"
	Sino si Z=2 Escribir "El jugador 2 eligio piedra"
		SIno si Z=3 Escribir "El jugador 2 eligio tijera"
				
			FinSi
		FinSi
	FinSi
	Si X=Z Entonces
		resultado=1
	Sino si X=1 y Z=3 o X=2 y Z=1 o X=3 y Z=2
			resultado=2
			Si no resultado=3
			FinSi
		FinSi
	FinSi
	
	Segun resultado
		caso 1: Escribir "Resultado de la segunda ronda es empate"
		caso 2: Escribir "Resultado de la segunda ronda es ganador jugador 2"
		caso 3: Escribir "Resultado de la segunda ronda es ganador jugador 3"
			
	fin segun 
	X=Aleatorio(1,3)
	Si X=1 Entonces Escribir "El jugador 1 eligio papel"
	Sino si X=2 Escribir "El jugador 1 eligio piedra"
		SIno si X=3 Escribir "El jugador 1 eligio tijera"
				
			FinSi
		FinSi
	FinSi
	Z=Aleatorio(1,3)
	Si Z=1 Entonces Escribir "El jugador 2 eligio papel"
	Sino si Z=2 Escribir "El jugador 2 eligio piedra"
		SIno si Z=3 Escribir "El jugador 2 eligio tijera"
				
			FinSi
		FinSi
	FinSi
	Si X=Z Entonces
		resultado=1
	Sino si X=1 y Z=3 o X=2 y Z=1 o X=3 y Z=2
			resultado=2
			Si no resultado=3
			FinSi
		FinSi
	FinSi
	
	Segun resultado
		caso 1: Escribir "Resultado de la tercera ronda es empate"
		caso 2:  Escribir "Resultado de la tercera ronda es ganador jugador 2"
		caso 3: Escribir "Resultado de la tercera ronda es ganador jugador 3"
			
	fin segun 
FinFuncion

funcion JuegoDeLosDados(nickname1,nickname2)
	//alumno2 Jorge Cabrera
	escribir "Bienvenidos al juego de los dados"
	
	imprimir "Primera Ronda"
	Dado1 = ALEATORIO(1,6)
	Dado2 = ALEATORIO(1,6)
	Imprimir "El jugador ",nickname1," obtuvo ", Dado1
	Imprimir "El jugador ",nickname2," obtuvo ", Dado2
	Si Dado1 = Dado2
		Ganador1 = nickname1
	Sino 
		Ganador1 = nickname2
	FinSi
	Imprimir "El ganador de la primera ronda es ",Ganador1
	
	
	Imprimir "Segunda Ronda"
	Dado3 = ALEATORIO(1,6)
	Dado4 = ALEATORIO(1,6)
	Imprimir "El jugador ",nickname1," obtuvo ", Dado3
	Imprimir "El jugador ",nickname2," obtuvo ", Dado4
	Si Dado3 = Dado4
		Ganador2 = nickname1
	Sino 
		Ganador2 = nickname2
	Fin si
	imprimir "El ganador de la segunda ronda es ",Ganador2
	
	
	imprimir "Tercera Ronda"
	Dado5 = ALEATORIO(1,6)
	Dado6 = ALEATORIO(1,6)
	Imprimir "El jugador ",nickname1," obtuvo ", Dado5
	Imprimir "El jugador ",nickname2," obtuvo ", Dado6
	Si Dado5 = Dado6
		Ganador3 = nickname1
	Sino 
		Ganador3 = nickname2
	FinSi
	imprimir "El ganador de la tercera ronda es ",Ganador3
	
	
	Si ganador1 = nickname1 y ganador2 = nickname1 y ganador3 = nickname1
		ganadorDefinitivo = nickname1
	Sino si ganador1 = nickname1 y ganador2 = nickname1 y ganador3 = nickname2
			ganadorDefinitivo = nickname1
		Sino si ganador1 = nickname1 y ganador2 = nickname2 y Ganador3 = nickname1
				ganadorDefinitivo = nickname1
			sino si ganador1 = nickname2 y ganador2 = nickname1 y ganador3 = nickname1
					ganadorDefinitivo = nickname1
				sino si ganador1 = nickname2 y ganador2 = nickname2 y ganador3 = nickname2
						ganadorDefinitivo = nickname2
					sino si ganador1 = nickname2 y ganador2 = nickname2 y ganador3 = nickname1
							ganadorDefinitivo = nickname2
						sino si ganador1 = nickname2 y ganador2 = nickname1 y ganador3 = nickname2
								ganadorDefinitivo = nickname2
							sino si ganador1 = nickname1 y ganador2 = nickname2 y ganador3 = nickname2
									ganadorDefinitivo = nickname2
								FinSi
							FinSi
						Finsi		
					FinSi
				FinSi
			finsi
		finsi
	finsi
	Imprimir "El ganador de juego es ",ganadorDefinitivo
Fin funcion

Funcion acertadaJugador1=ronda(nickname1,nickname2,respuesta1)
	numeroAleatorio=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
	Si respuesta1=digitoDelMedio Entonces
		Imprimir "Felicidades acertaste", nickname1
		acertadaJugador=1
		
	SiNo
		Escribir "incorrecto te quedan 2 intentos :D"
		Leer respuesta1
		Si respuesta1=digitoDelMedio Entonces
			Imprimir "Felicidades acertaste", nickname1
			acertadaJugador=1
			
		SiNo
			Escribir "incorrecto te quedan 1 intento :D"
			Leer respuesta1
			
			Si respuesta1=digitoDelMedio Entonces
				Imprimir "Felicidades acertaste", nickname1
				acertadaJugador=1
			SiNo
				Imprimir "perdiste todos tus intentos", nickname1
				acertadaJugador=0
			Fin Si
		Fin Si
	Fin Si
	acertadaJugador1=0+acertadaJugador
FinFuncion

Funcion acertadaJugador2=rondaa(nickname1,nickname2)
	Escribir "Turno Del " nickname2
	leer respuesta2
	numeroAleatorio=aleatorio(100,999)
	aleatorioEnCaracter=ConvertirATexto(numeroAleatorio)
	digitoDelMedio=ConvertirANumero(subcadena(aleatorioEnCaracter,2,2))
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
FinFuncion



funcion NumeroDelMedio(nickname1,nickname2)
	Imprimir digitoDelMedio
	Escribir nickname1, " intenta adivinar el numero del medio del numero aleatorio"
	Leer respuesta1
	acertadaJugador1=ronda(nickname1,nickname2,respuesta1)
	jugadorRonda1=acertadaJugador1
	imprimir digitoDelMedio
	Escribir "Turno Del jugador2"
	leer respuesta2
	
	
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
		Imprimir "Felicidades acertaste "
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




Algoritmo juegosMultiples
	nickname1= calculo()
	nickname2=calculo2()
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	Imprimir "Por favor seleccion un juego"
	Imprimir "1.-Piedra papel o tijeras"
	Imprimir "2.-Dados"
	Imprimir "3.-Numero del medio"
	Imprimir "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
	leer respuesta
	Segun respuesta Hacer
		1:
			PiedraPapelTijera(nickname1,nickname2)
		2:
			JuegoDeLosDados(nickname1,nickname2)
		3:
			NumeroDelMedio(nickname1,nickname2)
		De Otro Modo:
			Imprimir "opcion invalida"
	Fin Segun
FinAlgoritmo

