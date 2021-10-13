# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
urppercase_fruits = [x.upper() for x in fruits]

print(urppercase_fruits)

#Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

def count_vowels(x):
    vowels = ["a","A", "e", "E", "i", "I", "o", "O", "u", "U"]
    number_of_vowels = [each for each in x if each in vowels]
    
    return len(number_of_vowels)

fruits_with_more_than_two_vowels = []
for fruit in fruits:
    if count_vowels(fruit) > 2:
        fruits_with_more_than_two_vowels.append(fruit)
print(fruits_with_more_than_two_vowels)
        
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
def count_vowels(x):
    vowels = ["a","A", "e", "E", "i", "I", "o", "O", "u", "U"]
    number_of_vowels = [each for each in x if each in vowels]
    
    return len(number_of_vowels)

fruits_with_two_vowels = []
for fruit in fruits:
    if count_vowels(fruit) == 2:
        fruits_with_two_vowels.append(fruit)
print(fruits_with_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters

def count_char(x):
    
    number_of_char = [each for each in x if each in fruit]
    
    return len(number_of_char)

fruits_with_more_than_five_char = []
for fruit in fruits:
    if count_char(fruit) > 5:
        fruits_with_more_than_five_char.append(fruit)
print(fruits_with_more_than_five_char)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

def count_char(x):
    
    number_of_char = [each for each in x if each in fruit]
    
    return len(number_of_char)

fruits_with_exactly_five_char = []
for fruit in fruits:
    if count_char(fruit) == 5:
        fruits_with_exactly_five_char.append(fruit)
print(fruits_with_exactly_five_char)


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
def count_char(x):
    
    number_of_char = [each for each in x if each in fruit]
    
    return len(number_of_char)

fruits_with_lessthan_five_char = []
for fruit in fruits:
    if count_char(fruit) < 5:
        fruits_with_lessthan_five_char.append(fruit)
print(fruits_with_lessthan_five_char)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]