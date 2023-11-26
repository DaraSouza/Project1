my_favourite_fruits = ["mangoes", "oranges", "pineapples", "grapes", "lemons"]
for fruit in my_favourite_fruits:
    print("I like", fruit)

number_list = [9, 9, 11, 92]
total = 0

for num in number_list:
    total += num

print("Sum of numbers", total)

import random

random_number = random.randint(1, 20)
guess = 0


guess = int(input("Guess the number (between 1, 20): "))
if guess < random_number:
    print("Too low! Please try again")
elif guess > random_number:
    print("Too high! Please try again")
else:
    print("You guessed the right number. I'm very proud of you!")
    
    

password = "wintery123"

while True
while password != 8:
    print("Try again please")
if guess > 8:
    print("Your number is too high, try again.")
elif guess < 8:
    print("Your guess is too low, try again.")
else: 
    print("You guessed the password, you have unlocked a gold chest.")
