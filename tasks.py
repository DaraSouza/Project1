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


while guess != random_number:
    guess = int(input("Guess the number (between 1, 20): "))
if guess > random_number:
    print("Too high! Please try again")
else:
    print("You guessed the right number. I'm very proud of you!")
    
    

password = "wintery123"
user_input = input("Enter the password: ")
while guess == password:
    print("Yay!! You guessed the password.")

if guess != password:
    print("Are you breaking in?! I got my eyes on you.")
