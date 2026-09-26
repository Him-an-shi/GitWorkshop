import random
secret = random.randint(1, 10)
print("Guess a number from 1 to 10")
for _ in range(3):
    guess = int(input("Your guess: "))
    if guess == secret:
        print("Correct!")
        break
    print("Try again!")
print("The number was:", secret)