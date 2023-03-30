Algoritmo JuegoDeLosDados
	Definir jugador1,jugador2 Como Caracter
	escribir "Bienvenidos al juego de los dados"
	escribir "Escriba el nombre del jugador 1"
	leer jugador1
	escribir "Escriba el nombre del jugador 2"
	leer jugador2
	
	
	imprimir "Primera Ronda"
	Dado1=ALEATORIO(1,6)
	Dado2=ALEATORIO(1,6)
	Imprimir "El jugador ",jugador1," obtuvo ", Dado1
	Imprimir "El jugador ",jugador2," obtuvo ", Dado2
	Si Dado1=Dado2
		Ganador1=jugador1
	Sino 
		Ganador1=jugador2
	FinSi
	Imprimir "El ganador de la primera ronda es ",Ganador1
	
	
	Imprimir "Segunda Ronda"
	Dado3=ALEATORIO(1,6)
	Dado4=ALEATORIO(1,6)
	Imprimir "El jugador ",jugador1," obtuvo ", Dado3
	Imprimir "El jugador ",jugador2," obtuvo ", Dado4
	Si Dado3=Dado4
		Ganador2=jugador1
	Sino 
		Ganador2=jugador2
	Fin si
	imprimir "El ganador de la segunda ronda es ",Ganador2
	
	
	imprimir "Tercera Ronda"
	Dado5=ALEATORIO(1,6)
	Dado6=ALEATORIO(1,6)
	Imprimir "El jugador ",jugador1," obtuvo ", Dado5
	Imprimir "El jugador ",jugador2," obtuvo ", Dado6
	Si Dado5=Dado6
		Ganador3=jugador1
	Sino 
		Ganador3=jugador2
	FinSi
	imprimir "El ganador de la tercera ronda es ",Ganador3
	
	
	Si ganador1=jugador1 y ganador2=jugador1 y ganador3=jugador1
		ganadorDefinitivo=jugador1
	Sino si ganador1=jugador1 y ganador2=jugador1 y ganador3=jugador2
			ganadorDefinitivo=jugador1
		Sino si ganador1=jugador1 y ganador2=jugador2 y Ganador3=jugador1
				ganadorDefinitivo=jugador1
			sino si ganador1=jugador2 y ganador2=jugador1 y ganador3=jugador1
					ganadorDefinitivo=jugador1
				sino si ganador1=jugador2 y ganador2=jugador2 y ganador3=jugador2
						ganadorDefinitivo=jugador2
					sino si ganador1=jugador2 y ganador2=jugador2 y ganador3=jugador1
							ganadorDefinitivo=jugador2
						sino si ganador1=jugador2 y ganador2=jugador1 y ganador3=jugador2
								ganadorDefinitivo=jugador2
							sino si ganador1=jugador1 y ganador2=jugador2 y ganador3=jugador2
									ganadorDefinitivo=jugador2
						    FinSi
				        FinSi
		            Finsi		
			    FinSi
		    FinSi
	    finsi
finsi
finsi
Imprimir "El ganador de juego es ",ganadorDefinitivo
	Fin Algoritmo
	
