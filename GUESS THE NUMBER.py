import random

comp_num = random.randint(1, 100)

print("Welcome Pratham ")
print("Welcome to Guess the Number Game!")
while True:
    guess = int(input("Enter your guess: "))

    if guess < comp_num:
        print("Too low! Try again.")
    elif guess > comp_num:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed the correct number.🎉")
        break