import random #this library will help us to create a random number

def numeroAleatorio(numMay):		#funcion para crear numero aleatorio
	return random.randint(1, numMay)

print("Lets play a game, you need to guess a number between 1 and the number you choose")
numMay = int(input("Which number will you choose?"))	#asking the number to the user to make the range
randNum = numeroAleatorio(numMay)
print("The range is 1 - " + str(randNum))
