import random

print("Number Guessing Game")
num = random.randint(1,9)

chance = 0

print("guess the number between 1 to 9")

while chance < 3:

    guess = int(input("Enter your guess"))
    if guess == num:
        print("Congratulation you have guessed correctly")
        break
    elif guess < num:
        print("Your guess was too low. Guess a number higher than ",guess)
    else:
      print("Your guess was too high. Guess a number lower than", guess)
    chance = chance + 1

if not chance < 3:

    print("you lose. The number is", num)