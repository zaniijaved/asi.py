#Create a function* that takes an array, an index, and a value as parameters.
#  Inside the function, use the insert method to insert the value at the specified 
# index in the array. Return the modified array.
def insert_value(arr, index, value):
    arr.insert(index, value)
    return arr

my_array = [1, 2, 3, 5]
updated_array = insert_value(my_array, 3, 4)
print(updated_array)
#Write a program* that uses a while loop to print the first 25 integers.
i = 1
while i <= 25:
    print(i)
    i += 1

#Write a program* that uses a while loop to print the first 10 even numbers.
count = 1
num = 2
while count <= 10:
    print(num)
    num += 2
    count += 1

#Create a function* that takes a positive integer as a parameter and
#  uses a while loop to calculate and return the factorial of that number.
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

number = int(input("Enter a positive integer: "))
print("Factorial of", number, "is", factorial(number))

#Create a function* that takes an array of numbers as a parameter.
#  Use a while loop to calculate and return the sum of all the numbers in the array.
def sum_of_array(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total

numbers = [4, 7, 2, 9, 6]
print("Sum of the array:", sum_of_array(numbers))

#Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.
def remove_negative_numbers(numbers):
    # Use list comprehension to filter out negative numbers
    positive_numbers = [num for num in numbers if num >= 0]
    return positive_numbers
array_of_numbers = [10, -5, 3, -1, 0, 7, -8, 2]
result = remove_negative_numbers(array_of_numbers)

print("Original array:", array_of_numbers)
print("Array after removing negatives:", result)


# Implement a program* that takes a list of temperatures in Celsius as input from the user.
#  Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32
#  and store the converted temperatures in an array.
#  Use a while loop to perform the conversion for each temperature.
def celsius_to_fahrenheit(celsius_temps):
    fahrenheit_temps = []
    i = 0
    while i < len(celsius_temps):
        fahrenheit = (celsius_temps[i] * 9/5) + 32
        fahrenheit_temps.append(fahrenheit)
        i += 1
    return fahrenheit_temps

celsius_temps = []

n = int(input("How many temperatures do you want to convert? "))

i = 0
while i < n:
    temp = float(input(f"Enter temperature {i+1} in Celsius: "))
    celsius_temps.append(temp)
    i += 1

fahrenheit_temps = celsius_to_fahrenheit(celsius_temps)
print("Temperatures in Fahrenheit:", fahrenheit_temps)


# Write a program* to remove all the odd numbers from an array.
def remove_odd_numbers(numbers):
    even_numbers = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0: 
            even_numbers.append(numbers[i])
        i += 1
    return even_numbers

numbers = [10, 15, 22, 33, 40, 55, 60]
filtered_numbers = remove_odd_numbers(numbers)
print("Array after removing odd numbers:", filtered_numbers)

