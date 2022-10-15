# Importing Module
import random


# Printing Welcome Message
print("Welcome to Number Guessing Game!")
print("--------------------------------------------------")

# Creating a function that will compare user number and original number and show the result
def show_result(user_number,original_number):
    if user_number == original_number:
        print("Hurray, you guess the right number!")
    else:
        print(f"Sorry, you guess the wrong number. The right one is {original_number}.")


# Taking a random number
original_number = random.randint(1,10)

# Printing the hint
print("The number is between 1 to 10 including 1 and 10")
print("----------------------------------------------------------")

# Taking User Input
user_number = int(input("Guess the number: "))


# Showing the result
show_result(user_number=user_number,original_number=original_number)

