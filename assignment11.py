print("Welcome to the Adventure Game!")
choice = input("You find a treasure chest. Do you want to 'open' or 'leave' it")
if choice == "open":
    print("You found a treasure! You win the game!")
elif choice == "leave":
    print("You decided to leave the chest. The adventure continues.")
else:
    ("Invalid choice. Please decide to 'open' or 'leave' the treasure chest.")
