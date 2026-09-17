import Module
import datetime
import time
import random
import uuid
import math
import sys
import string

def datetime_operations():
    '''
    Performs different date and time related operations.
    This function allows user to 
    1.Display the current date and time
    2.Calculate the difference between two dates
    3.Format the current date using a custom format
    4.Run a stopwatch
    5.Run a countdown timer
    Returns: None

    '''
    while True:

     print("-----------------------")
     print("Date and Time operations: ")
     print("1. Display current date and time")
     print("2. Calcultate difference between two dates/times")
     print("3. Format date into custom format")
     print("4. Stopwatch")
     print("5. Countdown Timer")
     print("6. Back to main Menu")

     choice = input("Enter your choice: ").strip()

     if choice == '1':
        now = datetime.datetime.now()
        print(f"Current date and time: {now.strftime('%y-%m-%d %H:%M:%S')}")

     elif choice == '2':
        try:
            d1_str = input("Enter the first date(YYYY-MM-DD): ")
            d2_str = input("Enter the second date(YYYY-MM-DD): ")
            d1 = datetime.datetime.strptime(d1_str,"%Y-%m-%d")
            d2 = datetime.datetime.strptime(d2_str,"%Y-%m-%d")

            diff = abs((d2-d1).days)
            print(f"Difference: {diff} days")
        except ValueError:
            print("Invalid date format.Please use YYYY-MM-DD.")

     elif choice == '3':
        try:
            fmt = input("Enter custom strftime format(%A,%B,%d,%Y): ")
            print(f"Formattes Date: {datetime.datetime.now().strftime(fmt)}")
        except Exception as e:
            print(f"Error formatting date: {e}")

     elif choice == '4':
        print("Stopwatch started. Press ctrl+C to stop.")
        start_time = time.time()
        try:
            while True:
                elapsed = time.time() - start_time
                print(f"Elapsed Time: {elapsed:.2f} seconds",end="",flush=True)
                time.sleep(0.1)

        except KeyboardInterrupt:
            elapsed = time.time() - start_time
            print(f"\nStopwatch stopped. Total Time: {elapsed:.2f} seconds")

     elif choice == '5':
        try:
            seconds = int(input("Enter countdown time in seconds: "))
            print("Countdown Starting..")
            while seconds > 0:
                print(f"Time remaining: {seconds} seconds",
                      end="\r",
                      flush=True)
                
                time.sleep(1)
                seconds -= 1
            print("\nTime's up!")
        except ValueError:
            print("Please enter a valid integer.")

     elif choice == '6':
        break

def mathematical_operations():
    '''
    Performs Different mathematical calculations.
    Allows user to
    1.Calculate factorial
    2.Calculate compound interest
    3.Perform triginimetric calculation
    4.Calculate the area of geometric shapes
    Returns: None
    '''
    while True:

     print("-----------------------------------")
     print("Mathematical Operations:")
     print("1. Calculate Factorial")
     print("2. Solve Compound Interest")
     print("3. Trigonometric Calculations")
     print("4. Area of Geometric Shapes")
     print("5. Back to main Menu")

     Choice = input("Enter your choice: ").strip() 
     if Choice == '1':
        try:
            num = int(input("Enter a number:"))
            if num < 0:
                print("Factorial is not deined for negative numbes.")
            else:
                print(f"Factorial: {math.factorial(num)}")
        except ValueError:
            print("Invalid Input. Please enter an integer")

     elif Choice == '2':
        try:
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest(in %): "))
            t = float(input("Enter time(in years): "))
            amount = p * (math.pow((1+(r / 100)),t))
            compund_interest = amount - p
            print(f"Compund Interest: {compund_interest:.2f}")
        except ValueError:
            print("Invalid numerical input.")

     elif Choice == '3':
        try:
            deg = float(input("Enter angle in degrees: "))
            rad = math.radians(deg)
            print(f"Sin({deg}): {math.sin(rad):.4f}")
            print(f"Cos({deg}): {math.cos(rad):.4f}")
        except ValueError:
            print("Invalid Input.")

     elif Choice == '4':
        print("Select Shape:")
        print("1. Circle")
        print("2. Rectangle")
        shape_choice = input("Enter your choice: ")
        if shape_choice == '1':
            r = float(input("Enter radius: "))
            print(f"Area of Circle: {math.pi * r * r:.4f}")
        elif shape_choice == '2':
            l = float(input("Enter Length: "))
            w = float(input("Enter Width: "))
            print(f"Area of Rectangle: {l * w:.4f}")
        else:
            print("Invalid Choice")
     elif Choice == '5':
         break
     
def random_data_generation():
    '''
    Generates different types of random data
    Allows user to
    1.Genrate a random number
    2.Generate a random list
    3.Create a random password.
    4.Generate a random OTP.
    Returns : None
    '''
    while True:
        print("----------------------------------------")
        print("Random Data Generation: ")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                low = int(input("Enterminimum value: "))
                high = int(input("Enter maximum value: "))
                print(f"Generated Random Numbers: {random.randint(low,high)}")
            except ValueError:
                print("Invalid integers.")

        elif choice == '2':
            try:
                size = int(input("Enter size of the list: "))
                low = int(input("Enter minimum element value: "))
                high = int(input("Enter maximum element value: "))
                random_list = [random.randint(low,high) for _ in range(size)]

                print(f"Generated Random List: {random_list}")

            except ValueError:
                print("Invalid Input")

        elif choice == '3':
            try:
                length = int(input("Enter password length: "))
                if length <= 0:
                    raise ValueError("Length must be greater than zero.")
                charcter = string.ascii_letters + string.digits + string.punctuation
                password = "".join(random.choices(charcter, k=length))
                print(f"Generated Password: {password}")

            except ValueError as e:
                print("Invalid Input")

        elif choice =='4':
            otp = "".join(random.choice("0123456789") for _ in range(6))
            print(f"Generated 6-Digit OTP: {otp}")

        elif choice == '5':
            break

def genrated_uuid_menu():
    '''
    Generates and display a unique identifier(UUID)
    UUID is a universaally unique identifier generated using the uuis module.
    Returns: The function displays the generated UUID and does not return a value.
    '''
    print("--------------------------------------------")
    print("Generated Unique Identifiers(UUID): ")
    print(f"Generated UUID: {uuid.uuid4()}")

def file_operation_menu():
    '''
    Provides file handling operations using the custom Module.py file
    Allows user to
    1.Create a new file
    2.write data into a file
    3.read data from a file
    4.append data to a file
    Parameters:
    This fuctions does not require any parameters
    '''
    while True: 
        print("------------------------------------------")
        print("File Operations (Custom Module)")    
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            filename = input("Enter file name: ")
            Module.create_file(filename)
        elif choice == '2':
            filename = input("Enter file name: ")
            content = input("Enter data to write: ")
            Module.write_file(filename,content)
        elif choice == '3':
            filename = input("Enter file name: ")
            Module.read_file(filename)
        elif choice == '4':
            filename = input("Enter file name: ")
            content = input("Enter data to append: ")
            Module.append_file(filename,content)
        elif choice == '5':
            break

def explre_modules():
    '''
    Explores and displays the available attributes of a selected module.
    Supported modules:
        datetime,time,math,random,uuid,Module and String.
    '''
    print("---------------------------------------------")
    print("Explore Module Attributes (dir())")
    mod_name = input("Enter module name to explore(e.g, math,random)")

    if mod_name in ['datetime','time','math','random','uuid','Module','string']:
        try:
            module_obj = __import__(mod_name)
            attributes = dir(module_obj)
            print(f"Available Attributes in {mod_name} module: ")
            print(attributes[:10],"...")
        except Exception as e:
            print("Error exploring module: {e}")

    else:
        print(f"Module '{mod_name} is not part of the toolkit baseline.")

print("-------------------------------------------")
print("Documentation of Multi-Utility Toolkit")
print("-------------------------------------------")
print("1. datetime_operation() Documentation:")
print("--------------------------------------------")
print(datetime_operations.__doc__)

print("2. mathematical_operations() Documentation:")
print("--------------------------------------------")
print(mathematical_operations.__doc__)

print("3. random_data_generation() Documentation:")
print("--------------------------------------------")
print(random_data_generation.__doc__)

print("4. generated_uuid_menu() Documentation:")
print("----------------------------------------")
print(genrated_uuid_menu.__doc__)

print("5. file_operation_menu() Documentation:")
print("-----------------------------------------")
print(file_operation_menu.__doc__)

print("6. explore_modules() Documentation:")
print("----------------------------------------")
print(explre_modules.__doc__)

print("Create_file() Docuentation:")
print("------------------------------------------")
print(Module.create_file.__doc__)

print("write_file() Documentation:")
print("---------------------------------------------")
print(Module.write_file.__doc__)

print("read_file()Documentation:")
print("------------------------------------------------")
print(Module.read_file.__doc__)

print("append_file() Documentation:")
print("---------------------------------------------------")
print(Module.append_file.__doc__)

'''
The main program displays the Multi-Utility Toolkit menu
and calls the approproiate function according to user's choice.
'''
if __name__ == '__main__':
    while True:
        print("-------------------------------------------")
        print("Welcome to Multi-Utility Toolkit")
        print("--------------------------------------------")
        print("Choose an Option")
        print("1. Datatime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generations")
        print("4. Generate Unique Identifiers(UUID)")
        print("5. File Operations(Custome Module)")
        print("6. Explore Module Attributes(dir())")
        print("7. Exit")

        main_choice = input("Enter your choice: ")
        if main_choice == '1':
            datetime_operations()
        elif  main_choice == '2':
            mathematical_operations()
        elif main_choice == '3':
            random_data_generation()
        elif main_choice == '4':
            genrated_uuid_menu()
        elif main_choice == '5':
            file_operation_menu()
        elif main_choice == '6':
            explre_modules()
        elif main_choice == '7':
            print("Thank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid Choice.Please select from option 1 to 7.")