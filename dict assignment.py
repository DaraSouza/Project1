# Example 1: Dictionary of ages

ages = {"Alice" : 10, "Bob" : 12, "Charlie": 11, "David" : 9, "Eva": 13}
print("Dictionary of ages", ages)

# Example 2: Dictionary of book titles and their authors
books = {"Python Crash Course" : "Eric Matthes", "Deep Learning"  : "Ian Goodfellow"}
print("Dictionary of book", books)

# Example 3: Dictionary of superhero powers
superheroes = {"Superman" : "Flying", "Batman" : "Gadgets", "Wonder Woman" : "Lasso of Truth"}
print("Dictionary of superheroes", superheroes)

# Example 4: Accessing elements in a dictionary
alice_age = ages ["Alice"]
print("Alice's age:", alice_age)

book_author = books["Python Crash Course"]
print("Author of Python Crash Course:", book_author)

# Example 5: Modifying dictionaries
ages["Eva"] = 14
print("Updated ages:", ages)

books["Deep Learning"] = "Yoshua Bengio"
print("Updated books:", books)

superheroes["Batman"] = "Utility Belt"
print(" Updated superheroes:", superheroes)