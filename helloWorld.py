# This script gathers information on the user and its pet

name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")

# Print out the information
print(f"Hi {name} {surname}! You're {age} years old and have the email: {email}!")

# Ask user for pet information
pet_name = input("Enter your pet's first name: ")
pet_surname = input("Enter your pet's surname: ")
pet_age = int(input("Enter your pet's age: "))

# Print pet information
print(f"Your pet's name is {pet_name} {pet_surname} and it's age is {pet_age}!")
