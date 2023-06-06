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
