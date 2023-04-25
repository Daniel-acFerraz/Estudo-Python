secretWord = "giraffe"
guess = ""
guessCount = 3
while guess != secretWord:
    guess = input("Enter guess (" + str(guessCount) +" attempts left): ")
    guessCount -= 1
    if guessCount <= 0:
        print("Sorry, better luck next time!")
        break
    if guess == secretWord:
        print("You win!")
        break