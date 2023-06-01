import random #this library will help us to create a random number

def numeroAleatorio(numMay):		#funcion para crear numero aleatorio
	return random.randint(1, numMay)


name = input("Write your name ")
print("Hi " + name + "!") 		# variable tipo string para almacenar el nombre del usuario
print("Lets play a game, you need to guess a number between 1 and the number you choose")
numMay = int(input("Which number will you choose? "))	#asking the number to the user to make the range
randNum = numeroAleatorio(numMay)
print("The range is 1 - " + str(numMay)) 	#printing the range

dato = 0 						# variable tipo int para leer el numero ingresado
cont = 1 						# variable tipo entero para contar los 
sino = "s" 						# variable tipo string para leer si el usuario desea seguir jugando
validar = True 					# variable tipo booleano para hacerle saber al programa que el usuario quiere seguir jugando
while validar == True: 						# empieza el ciclo while que servira para ejecutar el juego hasta que adivine el nombre o se acaben los intentos permitidos
	numero = numeroAleatorio() 		# crea un numero aleatorio para que el usuario lo adivine
	print("You have 10 tries to guess the number")
	dato = int(input("Write a number between 1 and " + numMay)) 			# lee el primer intento del usuario para adivinar el numero
	if numero != dato:											# valida si el numero ingresado es diferente al generado de manera aleatoria para continuar
		while cont!=10:											# while para ejecutar el juego hasta que se acaben los intentos permitidos
			if dato>numero: 									# valida si el numero es menor que el generado por el juego
				print("Muy alto, te quedan " + str(10-cont) + " intentos\n") 
				dato = int(input("Ingresa un numero entre el 1 y el 100 ")) 	#lee el nuevo intento del usuario
				cont = cont+1 									# aumenta el contador de intentos
			elif dato<numero: 									# valida si el numero es mayor al generado por el juego
				print("Muy bajo, te quedan " + str(10-cont) + " intentos\n") 
				dato = int(input("Ingresa un numero entre el 1 y el 100 ")) 	#lee el nuevo intento del usuario
				cont = cont+1 					# aumenta el contador de intentos
			elif numero == dato: 				# valida si el usuario adivino el numero
				print("Adivinaste el numero " + str(dato) + "!!!")		
				print("Excelente " + nombre +", lo lograste en " + str(cont) + " intentos")
				contPorcentaje += 1 							# aumenta el contador para saber las veces que se ha ejecutado el juego
				porcentaje = porcentaje + (cont/10)*100 		# calcula el porcentaje de aciertos que le ha tomado al usuario
				cont = 10 										# lleva el contador al tope para terminar el juego
	if cont==10 and numero!=dato:		
		print("Te quedaste sin intentos :( el numero era: " + str(numero))
	sino = input("Quieres jugar nuevamente? s/n") 		# lee la respuesta del usuario si queire jugar nuevamente
	if sino != "s":			# valida la respuesta del usuario
		validar = False
	cont = 1											#reinicia el contador
print("\nGracias por jugar " + nombre)
