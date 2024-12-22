# 1.What does the len() function do in Python? Write a code example using len() to find the length of a list.
# The len() function in Python is used to determine the length of an object.
# It returns the number of items in a container or the number of characters in a string.
l=[1,2,3,3,4,5]
print(l)
print("length of the list:",len(l))

#2.Write a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!".
name=input("Enter your name")
def greet():
    print("Hello",name)
greet()

#3.Write a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without using the built-in max() function.
numbers = [3, 7, 2, 8, 5, 10]
def find_maximum(numbers):
    max_value = numbers[0]  # Assume the first number is the maximum
    for i in numbers:  # Iterate through the list
        if i > max_value:  # Compare each number with the current max_value
            max_value = i  # Update max_value if a larger number is found
    return max_value  # Return the largest number
print("The maximum value is:", find_maximum(numbers))  # Output: The maximum value is: 10

#4.	Explain the difference between local and global variables in a Python function. Write a program where a global variable and a local variable have the same name and show how Python differentiates between them.
# Global Variables:Declared outside all functions.
#Local Variables:Declared inside a function.
# Global variable
x = 10
def my_function():
    # Local variable
    x = 5
    print("Inside the function, local x:", x)  # Refers to the local x
# Access the global variable
print("Outside the function, global x:", x)  # Refers to the global x
# Call the function
my_function()
# Access the global variable again
print("After the function call, global x:", x)  # Refers to the global x

#5.Create a function calculate_area(length, width=5) that calculates the area of a rectangle. If only the length is provided, the function should assume the width is 5. Show how the function behaves when called with and without the width argument.
def calculate_area(length, width=5):
    """
    Calculates the area of a rectangle.
    If width is not provided, it defaults to 5.
    """
    return length*width
# Case 1: Only length is provided
area1 = calculate_area(10)  # Width defaults to 5
print("Area when only length is provided:", area1)  # Output: 50
# Case 2: Both length and width are provided
area2 = calculate_area(10, 7)
print("Area when both length and width are provided:", area2)  # Output: 70
