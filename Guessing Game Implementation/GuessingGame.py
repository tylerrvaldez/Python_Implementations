# File: GuessingGame.py

# Date Created: 10/09/2020

# Date Last Modified: 10/09/2020

# Description of Program: The user will play a guessing game to see if they can guess the secret number the game has chosen.

# These two variables are to keep track of the secret number and the number of attempts the user has taken.
secretNum = 1458
numberOfAttempts = 0

welcome = print("Welcome to the guessing game. You have ten tries to guess my number.")

# While this loop runs the program will compare the user inputs to determine if 1) it is the secret number, 2) if it is out of range, or 3) if the user input is greater or lower than the secret number
while True:
  guess = input("Please enter your guess: ")
  if int(guess) == int(secretNum):
      print("That's correct")
      if numberOfAttempts == 0:
        print("Congratulations! You guessed it in on the first try!")
        break
      elif numberOfAttempts > 0:
        print("Congratulations! You guessed it in", numberOfAttempts+1, "guesses.")
        break
  elif int(guess)<=0 or int(guess)>=10000:
    print("Your guess must be between 0001 and 9999.")
    nextGuess = input("Please enter a valid guess: ")
    if int(nextGuess) == int(secretNum):
      print("That's correct")
      print("Congratulations! You guessed it in", numberOfAttempts+1, "guesses.")
      break
    elif int(nextGuess)>int(secretNum):
      numberOfAttempts += 1
      print("Your guess is too high.")
      print("Guesses so far:", numberOfAttempts)
    elif int(nextGuess)<int(secretNum):
      numberOfAttempts += 1
      print("Your guess is too low.")
      print("Guesses so far:", numberOfAttempts)
  elif int(guess)>int(secretNum):
    numberOfAttempts += 1
    print("Your guess is too high.")
    print("Guesses so far:", numberOfAttempts)
  elif int(guess)<int(secretNum):
    numberOfAttempts += 1
    print("Your guess is too low.")
    print("Guesses so far:", numberOfAttempts)
  if int(numberOfAttempts) == 10:
    print("Game over: you ran out of guesses.") 
    break
  else:
    continue