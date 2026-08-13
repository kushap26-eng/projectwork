# Functional Treat

data_type = []
def input_data():
    '''
    ----------------
    1) Input Data:
    ----------------
    This asks the user to enter either a 1D array or 2D array.
    It takes Integer value as input.
    It adds them to the global data list.
    Returns = 1. 1D list of intergers if user selects 1D
              2. 2D nested list of integer if the user selects 2D
    '''
    print("Choose array type: ")
    print("1. 1D array")
    print("2. 2D array")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        values = input("Enter values separated by space: ")
        data = list(map(int,values.split()))
        print("Data has been stored successfully!")
        data_type.extend(data)
        return data
    
    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        colums = int(input("Enter number of columns: "))
        array = []
        for i in range(rows):
            values = input(f'Enter values of row {i + 1}separated by space: ')
            rows = list(map(int,values.split()))
            if len(rows) != colums:
                print(f'Error: Expcted {colums} values,but got {len(rows)}')
            else:
                array.append(rows)
        for i in array:
            for j in i :
                data_type.append(j)

        print("Data has been stored successfully!")
        print(data_type)
        return array
       
def datasummary():
    '''
    ----------------
    2) Data Summary:
    -----------------
    Shows the basic structure and mathematical information of the the data using Python's built-in functions.
    Returns = Display the results
    '''
    global data_type
    
    print("Data Summary:")
    print("Total elements: ",len(data_type))
    print("Minimum value: ",min(data_type))
    print("Maximum value: ",max(data_type))
    print("Sum of all values: ",sum(data_type))
    print("Average value: ",sum(data_type) / len(data_type))

def factorial():
    '''
    -------------
    3) Factorial: 
    -------------
    Calculate and prints the factorial of a specified integer using recursion.
    Returns: Prints the calculated factorial of the number.'''
    def fact(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * fact(num-1)
    result = fact(num)
    print("Factorial of",num,"is:",result)
 
def filter_data():
    '''
    ----------------
    4) Filter Data:
    ----------------
    Filter data using a lambda function based on user threshold.
    Return: llist:A new list containing only the filtered numbers.'''
    global data_type

    if not data_type:
        print("No data available to filter.")
        return
    print("Choose filtering option:")
    print("1. Get numbers greater than a threshold")
    print("2. Get numbers less than a threshold")
    print("3. Get Even numbers")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        threshold = int(input("Enter threshold value: "))
        filtered = list(filter(lambda x: x>threshold,data_type))
        print(f"Numbers greater than {threshold}:{filtered}")
    elif choice == 2:
        threshold = int(input("Enter threshold value: "))
        filtered = list(filter(lambda x: x<threshold,data_type))
        print(f"Numbers less than {threshold}:{filtered}")
    elif choice == 3:
        filtered = list(filter(lambda x: x % 2 == 0,data_type))
        print(f"Even numbers:{filtered}")
    else:
        print("Invalid Choice.")

def sort_data():
    '''
    --------------
    5) Sort Data:
    --------------
    Sort data in ascending or descending order using built in functions.
    Returns: list: A new sorted list or none if the choice is invalid.'''
    global data_type
    if not data_type:
        print("No data available to sort.")
        return
    
    print("Choose Sorting order: ")
    print("1. Ascending order")
    print("2. Decending order")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sorted_data = sorted(data_type)
        print(f"Data in ascending order: {sorted_data}")
    elif choice == 2:
        sorted_data = sorted(data_type,reverse = True)
        print(f"Data in descending order: {sorted_data}")
    else:
        print("Invalid choice.")

def data_statistics(**kwargs):
    '''
    --------------------
    6) Data Statistics:
    ---------------------
    Calculate and return multiple statistical value using **kwargs dictionary foramatting.
    Args: 
    **kwargs: Arbitary keyword arguments.Accepts "dataset" to target specific data arrays.
    Returns: 
    tuple: Contains(total_elements,min_value,max_value,total_sum,avg_value)'''

    dataset = kwargs.get('dataset',data_type)
    total_elements =len(dataset)
    min_value = min(dataset)
    max_value = max(dataset)
    total_sum = sum(dataset)
    avg_value = total_sum / total_elements
    print("Dataset Summary using **kwargs: ")
    for key,value in kwargs.items():
        print("-",key,":",value)
    print(f"count:{total_elements}")
    print(f"Min:{min_value}")
    print(f"Max:{max_value}")
    print(f"Sum:{total_sum}")
    print(f"Average:{avg_value}")
    return total_elements,min_value,max_value,total_sum,avg_value



print("Welcome to the Data Analyzer and transformer programer")
while True:
    print("Main Menu:")
    print("1.Input Data")
    print("2.Display Data Summary(Built-in Function)")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter Data by Threshold(Lambda Function)")
    print("5.Sort data")
    print("6.Display Dataset Statistics(Return multiple values)")
    print("7.Exit Program")

    user_intput = int(input("Please enter your choice: "))
    if user_intput == 1:
        print(input_data())
    elif user_intput == 2:
        if not data_type:
            print("Error:No data available. Please select option 1 first.")
        else:
            datasummary()
    elif user_intput == 3:
        num = int(input("Enter a number to calculate its factorial: "))
        factorial()
    elif user_intput == 4:
        filter_data()
    elif user_intput == 5:
        sort_data()
    elif user_intput == 6:
        if not data_type:
            print("Error: No data available. Please select option 1 first.")
        else:
            data_statistics(dataset =data_type)
    elif user_intput == 7:
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        print(input_data.__doc__)
        print(datasummary.__doc__)
        print(factorial.__doc__)
        print(filter_data.__doc__)
        print(sort_data.__doc__)
        print(data_statistics.__doc__)
        break
        
    else:
        print("Invalid Choice. Please choose an option between 1 and 7.")