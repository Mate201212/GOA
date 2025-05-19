# Function to perform operations on three numbers
def perform_operations():
    # Input three numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Perform operations
    sum_result = num1 + num2 + num3
    diff_result = num1 - num2 - num3
    prod_result = num1 * num2 * num3
    if num2 != 0 and num3 != 0:  # Check to prevent division by zero
        div_result1 = num1 / num2
        div_result2 = num1 / num3
    else:
        div_result1 = "Undefined (division by zero)"
        div_result2 = "Undefined (division by zero)"

    # Display the results
    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {prod_result}")
    print(f"Division (num1 / num2): {div_result1}")
    print(f"Division (num1 / num3): {div_result2}")

# Call the function
perform_operations()



# Enter first name
first_name = input("Enter your first name: ")

# Enter last name
last_name = input("Enter your last name: ")

# Print the full name
print(f"Hello, {first_name} {last_name}! Welcome!")



# Input a string from the user
user_string = input("Enter a string: ")

# Multiply the string by five
string_result = user_string * 5  # Repeats the string five times

# Input a number from the user
user_number = float(input("Enter a number: "))  # Convert input to a float for multiplication

# Multiply the number by five
number_result = user_number * 5  # Multiplies the number by five

# Print both results
print(f"String Result: {string_result}")  # Displays the repeated string
print(f"Number Result: {number_result}")  # Displays the number multiplied by five