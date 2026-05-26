
# SMART DATA ANALYZER

summary = {}


# Function 1

def show_data(data):
    """Display all data"""
    print("Data =", data)


# Function 2

def calculate_average(data):
    """Calculate average"""
    avg = sum(data) / len(data)
    return avg



# Function 3

def find_max_min(data):
    """Find maximum and minimum"""
    return max(data), min(data)



# Function 4

def remove_duplicates(data):
    """Remove duplicate values"""
    return list(set(data))



# Function 5
def sort_data(data):
    """Sort the data"""
    return sorted(data)



# Function 6

def lambda_filter(data):
    """Filter values greater than 50"""
    
    result = list(filter(lambda x: x > 50, data))
    
    return result


# Function 7

def fibonacci(n):
    """Recursion example"""
    
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

# Function 8

def dataset_summary(data):
    """Global keyword example"""
    
    global summary
    
    summary["Total Values"] = len(data)
    summary["Sum"] = sum(data)
    
    print(summary)



# Function 9

def show_args(*args):
    """*args example"""
    
    print("Values are:")
    
    for i in args:
        print(i)


# Function 10

def show_kwargs(**kwargs):
    """**kwargs example"""
    
    for key, value in kwargs.items():
        print(key, ":", value)


# MAIN PROGRAM

data = list(map(int, input("Enter numbers: ").split()))

while True:

    print("\n===== SMART DATA ANALYZER =====")
    print("1. Show Data")
    print("2. Average")
    print("3. Max and Min")
    print("4. Remove Duplicates")
    print("5. Sort Data")
    print("6. Lambda Filter")
    print("7. Fibonacci")
    print("8. Dataset Summary")
    print("9. *args Example")
    print("10. **kwargs Example")
    print("11. Exit")

    choice = int(input("Enter choice: "))

    

    if choice == 1:
        show_data(data)

    elif choice == 2:
        print("Average =", calculate_average(data))

    elif choice == 3:
        maximum, minimum = find_max_min(data)

        print("Maximum =", maximum)
        print("Minimum =", minimum)

    elif choice == 4:
        print(remove_duplicates(data))

    elif choice == 5:
        print(sort_data(data))

    elif choice == 6:
        print(lambda_filter(data))

    elif choice == 7:
        n = int(input("Enter number: "))
        print("Fibonacci =", fibonacci(n))

    elif choice == 8:
        dataset_summary(data)

    elif choice == 9:
        show_args(10, 20, 30, 40)

    elif choice == 10:
        show_kwargs(Name="Nehal", Course="Python")

    elif choice == 11:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")