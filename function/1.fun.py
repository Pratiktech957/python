# reusability of code increses


def greet(name):
    print (f"Hello {name}, Welcome to Python Revolution")
    
greet("pratik")



def add(a,b):
    return a+b

result = add(5, 10)
print(f"The sum is: {result}")


# parameter vs arguments 

def greet(name):
    print(f"Hello {name}, Welcome to Python Revolution")
    
greet("pratik")  # "pratik" is an argument passed to the function greet

# possitional Arguments 

def greet(name,age):
    print(f"Hello {name}, You are {age} years old")
    
greet("pratik", 25)  # "pratik" and 25 are positional arguments

# keyword Arguments
def greet(name, age):
    print(f"Hello {name}, You are {age} years old")
    
greet(age=25, name="pratik")  # age and name are keyword arguments

# default Arguments
def greet(name="Guest"):
    print(f"Hello {name}, Welcome to Python Revolution")
greet()  # No argument passed, will use default value "Guest"

# reusability of code increases
# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return 3.14 * radius * radius
# Example usage
radius = float(input("Enter the radius of the circle: "))
circle_area = calculate_circle_area(radius)
print(f"The area of the circle is: {circle_area}")
# Function to check if a number is even or odd
def is_even(number):
    return number % 2 == 0
# Example usage
def check_even_odd(number):
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
check_even_odd(10)  # Output: 10 is even.
# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
    
    
    
    