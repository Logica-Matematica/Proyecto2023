Algoritmo PiedraPapelTijera
	Definir Jugador1, Jugador2,piedra,papel,tijera,ganador1,ganador2,ganador3 Como Caracter
	Definir ganador,ronda,resultado Como Entero
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
FinAlgoritmo
