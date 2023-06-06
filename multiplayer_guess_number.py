import getpass #It is the library for hiding characters 
plyo = input("What is your name: ")#Name of player one 
num_guess = int(getpass.getpass(plyo+", enter the number to be guessed: "))#we send to call to the library characteristics 

while True: #"While" loops to chose a number
    if num_guess>0 and num_guess<16:#Range to chose a number 
        break
    else:
        print ("The number is out of range")#Invalid number
plyt = input("Your name?: ") #Name of player two

score = 100  # Starting score for player 2
while score > 0: 
    guess = int(input(plyt+", try to guess the number: "))#Player 2 needs to guess the secret number 
     if (guess == num_guess) : #Comparision with the secret number
        print("Congratulations! You guessed the number correctly.")#message (if equal to the secret number)
        break
    else:
        score -= 10#If the answer is incorrect, subtract points
        print(f"Wrong guess! Your score is now " + str(score))#If the answer is incorrect, show the message
if score == 0: #comparision 
    print(plyo +"wins! ,", + plyt ," score reached 0.")# #if player 2 losse all points.