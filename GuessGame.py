import random

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber, maxNumber)

message = "The magic number is between {0} and {1}"
print(message.format(minNumber, maxNumber))

found = False
while not found:
    print("Guess what it is?")
    guessInput = input()

    if guessInput == "q":
        print("We're quitting as you wished")
        found = True
    else:
        guess = int(guessInput)
        if guess == magicNumber:
            print("You got it!")
            found = True

        if guess < magicNumber:
            print("Too low")

        if guess > magicNumber:
            print("Too high")

print("This is the end...")
