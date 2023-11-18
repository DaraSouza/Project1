print("Let's play the Animal Guessing game")
animal = input("I'm thinking of an animal. Is it a dog or a cat?")
if animal == "dog":
    print("Woof! You guessed it right, it's a dog!")
if animal == "cat":
    print("Meow! You guessed it right, it's a cat!")
else:
    print("Sorry, that's not one of the options. Try again with or dog or cat.")