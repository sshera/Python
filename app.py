from math import *
import useful_tools
from Student import Student
from Question import Question
from Chef import Chef
from SpecialChef import SpecialChef

# print("Hello World")
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")
# character_name = "John"
# character_age = "35"
# number_age = 35
# is_character = True
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old. ")
# character_name = "Mike"
# print("He really liked the name " + character_name + ", ")
# print("but he didn't like being " + character_age + ".")
# print("First line\nSecond line")
# print("This is in \"quote marks\"")
# phrase = "I'm storing this string inside a variable"
# print(phrase)
# print(phrase.lower())
# print(phrase.upper())
# print(phrase.isupper())
# print(phrase.upper().isupper())
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("v"))
# print(phrase.replace("I'm", "You're"))
# print(3 + 4.5)
# print(3 * (4 + 5))
# print(10 % 3)
# print(str(number_age) + " is my favorite number")
# my_number = -5
# print(abs(my_number))
# print(pow(2, 3))
# print(max(4, 9))
# print(min(4, 9))
# print(round(3.2))
# print(floor(3.7))
# print(ceil(3.1))
# print(sqrt(25))
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = int(num1) + float(num2)
# print(result)
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)
# print(friends[1])
# print(friends[1:])
# print(friends[1:3])
# friends[2] = "Mike"
# print(friends[2])
# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends.extend(lucky_numbers)
# friends.append("Jason")
# friends.insert(1, "Kelly")
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# friends.remove("Jim")
# friends.clear()
# friends.pop()
# print(friends.index("Kevin"))
# print(friends.count("Kevin"))
# friends.sort()
# print(friends)
# lucky_numbers.reverse()
# print(lucky_numbers)
# friends2 = friends.copy()
# print(friends2)
# coordinates = (4, 5)
# coordinate_array = [(4, 5), (6, 7), (80, 34)]
# tuples cannot be changed after declaration
# def say_hi(name):
# print("Hello " + name)


# say_hi("Mike")


# def cube(num):
# return num * num * num


# result = cube(3)
# print(result)
# return breaks us out of the function; we can't add further statements after it

# is_cat = True
# is_orange = False

# if is_cat or is_orange:
# print("You are a cat or orange or both")
# else:
# print("You are neither orange nor a cat")

# if is_cat and is_orange:
# print("You are an orange cat")
# elif is_cat and not (is_orange):
# print("You are a cat, but not orange")
# elif is_orange and not (is_cat):
# print("You are orange, but not a cat")
# else:
# print("You are neither orange nor a cat")


# def max_num(num1, num2, num3):
# if num1 >= num2 and num1 >= num3:
# return num1
# elif num2 >= num1 and num2 >= num3:
# return num2
# else:
# return num3


# print(max_num(3, 4, 5))

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator: ")

# if op == "+":
# print(num1 + num2)
# elif op == "-":
# print(num1 - num2)
# elif op == "/":
# print(num1 / num2)
# elif op == "*":
# print(num1 * num2)
# else:
# print("Invalid operator")

# month_conversions = {
# "Jan": "January",
# "Feb": "February",
# "Mar": "March",
# "Apr": "April",
# "May": "May",
# "Jun": "June",
# "Jul": "July",
# "Aug": "August",
# "Sep": "September",
# "Oct": "October",
# "Nov": "November",
# "Dec": "December",
# }

# print(month_conversions["Nov"])
# print(month_conversions.get("Mar"))
# print(month_conversions.get("Cat", "Not a valid key"))

# i = 1
# while i <= 10:
# print(i)
# i += 1
# i += 1 is same as i = i + 1
# print("Done with loop")

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not (out_of_guesses):
# if guess_count < guess_limit:
# guess = input("Enter guess: ")
# guess_count += 1
# else:
# out_of_guesses = True

# if out_of_guesses:
# print("Out of guesses, you lose")
# else:
# print("You win!")

# for letter in "My dog ate my homework":
# print(letter)

# friends = ["Jim", "Karen", "Kevin"]

# for friend in friends:
# print(friend)

# for index in range(10):
# print(index)
# start defaults to 0 unless specified otherwise with comma and stop is omitted for range

# for index in range(len(friends)):
# print(friends[index])

# for index in range(5):
# if index == 0:
# print("First iteration")
# else:
# print("Not first iteration")

# print(2**3)
# this is 2 to the power of 3


# def raise_to_power(base_num, pow_num):
# result = 1
# for index in range(pow_num):
# result = result * base_num
# return result


# print(raise_to_power(3, 4))

# number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

# print(number_grid[2][1])

# for row in number_grid:
# for element in row:
# print(element)


# def translate(phrase):
# translation = ""
# for letter in phrase:
# if letter.lower() in "bcdfghjklmnpqrstvwxz":
# if letter.isupper():
# translation = translation + "Sss"
# else:
# translation = translation + "sss"
# else:
# translation = translation + letter
# return translation


# print(translate(input("Enter a phrase: ")))

# try:
# number = int(input("Enter a number: "))
# print(number)
# except ValueError as err:
# print(err)

# cats_file = open("cats.txt", "r")
# read only mode

# print(cats_file.readable())
# print(cats_file.read())
# print(cats_file.readline())
# print(cats_file.readline())
# print(cats_file.readlines())
# puts the lines in an array

# for cat in cats_file.readlines():
# print(cat)

# cats_file = open("cats2.txt", "w")
# write mode; can change file

# cats_file.write("Duke - Abyssinian")

# cats_file = open("cats.txt", "a")
# append mode; can add info to end of file but can't modify info already in file

# cats_file.write("Mittens - tabby")
# cats_file.write("\nBubbles - Maine Coon")
# \n creates new line

# cats_file = open("cats.txt", "r+")
# read & write mode

# cats_file.close()
# remember to close file after opening

# print(useful_tools.roll_dice(20))

# student1 = Student("Jim", "Business", 3.1, True)
# print(student1.name)

# student2 = Student("Oscar", "Art", 3.8, False)

# question_prompts = [
# "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
# "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
# "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
# ]

# questions = [
# Question(question_prompts[0], "a"),
# Question(question_prompts[1], "c"),
# Question(question_prompts[2], "b"),
# ]


# def run_test(questions):
# score = 0
# for question in questions:
# answer = input(question.prompt)
# if answer == question.answer:
# score += 1
# print("You got " + str(score) + "/" + str(len(questions)) + " correct")


# run_test(questions)

# print(student1.on_honor_roll())
# print(student2.on_honor_roll())

my_chef = Chef()
my_chef.make_chicken()

your_chef = SpecialChef()
your_chef.make_special_dish()
