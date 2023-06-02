import random #this library will help us to create a random number

def numeroAleatorio(numMen, numMay):		#funcion para crear numero aleatorio
	return random.randint(1, numMay)

name = input("Write your name ")
print("Hi " + name + "!") 		# variable tipo string para almacenar el nombre del usuario
print("Lets play a game, you need to guess a number between two numbers that you'll choose")

dato = 0 						# variable tipo int para leer el numero ingresado
cont = 1 						# variable tipo entero para contar los 
sino = "y" 						# variable tipo string para leer si el usuario desea seguir jugando
validar = True 					# variable tipo booleano para hacerle saber al programa que el usuario quiere seguir jugando
while validar == True: 						# empieza el ciclo while que servira para ejecutar el juego hasta que adivine el nombre o se acaben los intentos permitidos
	while True:
	    try:
	    	firstNum = int(input("Write the first number "))	#asking the first number to the user to make the range
	    	break
	    except ValueError:
	        print("Oops!  That was no valid number.  Try again...")
	while True:
	    try:
	    	secondNum = int(input("Write the second number "))	#asking the second number to the user to make the range
	    	break
	    except ValueError:
	        print("Oops!  That was no valid number.  Try again...")
	if(firstNum>secondNum):
		num = numeroAleatorio(secondNum, firstNum)
		numMay = firstNum
		numMen = secondNum
	elif(firstNum<secondNum):
		num = numeroAleatorio(firstNum, secondNum)
		numMay = secondNum
		numMen = firstNum
	print("The range is " + str(numMen) + " - " + str(numMay)) 	#printing the range

	print("You have 10 tries to guess the number")
	while True:
		try:
			dato = int(input("Write a number between " + str(numMen) + " and " + str(numMay) + " ")) 	
			break
		except ValueError:
			print("Oops!  That was no valid number.  Try again...")		# lee el primer intento del usuario para adivinar el numero
	if num != dato:											# valida si el numero ingresado es diferente al generado de manera aleatoria para continuar
		while cont!=10:											# while para ejecutar el juego hasta que se acaben los intentos permitidos
			if dato>num: 									# valida si el numero es menor que el generado por el juego
				print("To high, you have " + str(10-cont) + " tries\n") 
				while True:
					try:
						dato = int(input("Write a number between " + str(numMen) + " and " + str(numMay) + " ")) 	#lee el nuevo intento del usuario
						break
					except ValueError:
						print("Oops!  That was no valid number.  Try again...")		# lee el primer intento del usuario para adivinar el numero
				cont = cont+1 									# aumenta el contador de intentos
			elif dato<num: 									# valida si el numero es mayor al generado por el juego
				print("To low, you have " + str(10-cont) + " tries\n") 
				while True:
					try:
						dato = int(input("Write a number between " + str(numMen) + " and " + str(numMay) + " ")) 	#lee el nuevo intento del usuario
						break
					except ValueError:
						print("Oops!  That was no valid number.  Try again...")		# lee el primer intento del usuario para adivinar el numero
				cont = cont+1 					# aumenta el contador de intentos
			elif num == dato: 				# valida si el usuario adivino el numero
				print("Congratulations! You guess the number " + str(dato) + "!!!")
				cont = (100-(cont*10))
				print("Excelent " + name +", you got " + str(cont) + " points")
				cont = 10 										# lleva el contador al tope para terminar el juego
	if cont==10 and num!=dato:		
		print("You don't have more tries, the number is: " + str(num))
	sino = input("Do you want to play again? y/n") 		# lee la respuesta del usuario si queire jugar nuevamente
	if sino != "y":			# valida la respuesta del usuario
		validar = False
	cont = 1											#reinicia el contador
print("\nThank u for playing " + name)
