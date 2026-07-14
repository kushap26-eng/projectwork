print("Welcome to the interactive personal Data Collector!")
name = input("Please enter your Name: ")
age = int(input("Please enter your Age: "))
height = float(input("Please enter your height in meters:"))
favourite_number =int(input("Please enter yourfavourite number: "))

birth_year = 2026 - age
print("\nThank you! Here is the information we collected:\n")

print("Name:",name,"(Type:",type(name),",Memory Address:",id(name),")")
print("Age:",age,"(Type:",type(age),",Memory Address:",id(age),")")
print("Height:",height,"(Type:",type(height),",Memory Address:",id(height),")")
print("Favourite Number:",favourite_number,"(Type:",type(favourite_number),",Memory Address:",id(favourite_number),")")

height_as_int = int(height)
print("\nType conversion Demonstration:")
print("Original Height:",height,"(float)")
print("Converted Height:",height_as_int,"(int)")


print("\nYour Birth year is approximately:",birth_year,"(based on your age of",age,")")

print("\nThank you for using the Personal Data Collector. Goodbye!") 