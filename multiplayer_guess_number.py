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
    guess = int(input(plyt+", try to guess the number: "))