# Writing a program that accepts user input to create a list of integers. 
# Then, computing the sum of all the integers in the list.
input_list = []
sum = 0
while True:
    user_input = input("Enter an integer (or 'q' to quit): ")
    if user_input == 'q':
        break
    input_list.append(int(user_input))
    sum += int(user_input)

print(f"The sum of the integers in the list is: {sum}")

# Creating a tuple containing the names of five of your favorite books. 
# Then, using a for loop to print each book name on a separate line.
favorite_books = ("The Hobbit", "The Lord of the Rings", "The Silmarillion", "The Silent Patient", "The Chronicles of Narnia")
for book in favorite_books:
    print(book)

# Writing a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.
person = {}
name = input("Enter your name: ")
person["name"] = name
age = input("Enter your age: ")
person["age"] = age
color = input("Enter your favorite color: ")
person["color"] = color
print(person)

# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.
set1 = set()
set2 = set()
while True:
    num = input("Enter an integer (or 'q' to quit): ")
    if num == 'q':
        break
    set1.add(int(num))
    set2.add(int(num))

common_set = set1.intersection(set2)

# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list 
# that contains only the words that have an odd number of characters.
words = ["hello", "world", "python", "code"]
odd_words = [word for word in words if len(word) % 2 != 0]
print(odd_words)


