## 💻 Exercises: Module 9

################################################################ Exercises: Level 1 ################################################################

# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def add_two_numbers(first_number, second_number):
   sum = first_number + second_number
   return sum

Total = add_two_numbers(10, 10)
print(Total)

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
def area_of_circle():
    radius = float(input("Input radius"))
    area = 3.142*radius**2
    print(area)

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"There is issue, '{arg}' is not a number. All arguments must be numeric."
    
    return sum(args)
x = add_all_nums(1,2,6)
print(x)

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def convert_celsius_to_fahrenheit(celsius):
    deg_sym = "\u00b0"
    fahrenheit = (celsius * 9/5) + 32
    return F"{fahrenheit}{deg_sym}F"

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_seasion(months):
    month = months.title()
    if month == "September" or month == "October" or month == "November":
        return "the season is Autumn"
    elif month == "December" or month == "January" or month == "February":
        return "the season is Winter"
    elif month == "March" or month == "April" or month == "May":
        return "the season is Spring"
    elif month == "June" or month == "July" or month == "August":   
        return " the season is Summer"
    else:
        return "Invalid Input"

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    # To avoid division by zero (that is when x1 == x2)
    if x2 - x1 == 0:
        return "The result is undefined"
    slope = (y2 - y1) / (x2 - x1)
    return slope

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
def _solve_quadratic_eqn(a, b, c):
    # discriminant is the expression under the square root of the quadratic equation
    discriminant = b**2 - 4*a*c
    
    # check wether the discriminant is positive or zero 
    if discriminant >= 0:
        result1 = (-b + discriminant**0.5) / (2*a)
        result2 = (-b - discriminant**0.5) / (2*a)
    else:
        # If discriminant is negative, calculate complex solutions
        real_part = -b / (2*a)
        imaginary_part = (abs(discriminant)**0.5) / (2*a)
        result1 = (imaginary_part)
        result2 = (real_part)
    
    return result1, result2

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(input_list):
    for item in input_list:
        print(item)

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    for array in reversed(array):
        print(array)

reverse = [1,2,3,4,5]    
reverse_list(reverse)

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
copy_list = ['banana', 'orange', 'mango', 'lemon']
copy_list = ['banana', 'orange', 'mango', 'lemon']
def capitalize_list_items(items):
    # Using a list comprehension to capitalize each item in the list
    return [item.capitalize() for item in items]
   
ret = capitalize_list_items(copy_list)
print(ret)

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
copy_list = ['banana', 'orange', 'mango', 'lemon']
def add_item(lst, item):
    lst.append(item)
    return lst
# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
copy_list = ['banana', 'orange', 'mango', 'lemon']
def remove_item(lst, item):
    lst.remove(item)
    return f"{lst}, \n{item} is the item that got removed'"

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    return sum(range(n + 1))

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

### Exercises: Level 2

################## 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    even = 0
    odd = 0
    if n < 0:
        return f"{n} is not a valid number, provide positive integer"
    else:
        for digit in str(n):
            if int(digit) % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1

    return f"The number of odd numbers are {odd}  \nThe number of even number are {even}"

# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
def _is_empty_(param):
    if not param:
        return "Please provide parameter"
    else:
        return f"{param} is the parameter you provide"

# 1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    sort_number = sorted(numbers)
    n = len(sort_number)
    if n % 2 == 1:
        return sort_number[n // 2]  
    else:
        return (sort_number[n // 2 - 1] + sort_number[n // 2]) / 2  

def calculate_mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_count = max(frequency.values())
    mode = [num for num, count in frequency.items() if count == max_count]
    return mode if len(mode) != len(numbers) else None 

def calculate_range(numbers):
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5  # Standard deviation is the square root of the variance

### Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    # Handle edge cases
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False  # Even numbers greater than 2 are not prime

    # Check divisibility from 3 to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False 
    return True 

# 1. Write a functions which checks if all items are unique in the list.
def are_all_items_unique(lst):
    # Check if the length of the list and the set are the same
    return len(lst) == len(set(lst))

# 1. Write a function which checks if all the items of the list are of the same data type.
def all_same_type(lst):
    first_item_type = type(lst[0])  
    for items in lst:
        if type(items) != first_item_type:
            return "The items in the list are of different data type"
    else:
        return "The items in the list are not of different data type"

# 1. Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    # to make sure the variable is non-empty and starts with a letter or underscore
    if not variable:
        return "Provide the variable name please"
    # to make sure the variable name starts with a letter or underscore
    if (variable[0].isdigit() or variable[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"):
        return "Variable must not start with Number"
    
    # to make sure the variable contains only valid characters (letters, digits, underscores)
    for char in variable:
        if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_":
            return False
        
    keywords = [
        "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue", "def",
        "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda",
        "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
    
    if variable in keywords:
        return "This is a keyword and cannot be used as a variable"
    else:
        return f"'{variable}' is a valid variable name"




'''1. Go to the data folder and access the countries-data.py file.
- Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
- Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.'''
import countries-data.py
def  most_spoken_languages_in_the_world():
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]
print(most_spoken_languages_in_the_world())
## 💻 List Comprehensions Exercises

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_num = [ num for num in numbers if num < 0]
print(neg_num)

# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lst = [listc for lista in list_of_lists for listb in lista for listc in listb]
print(lst)

# 3. Using list comprehension create the following list of tuples:
list = [(i,1,i,i*i,i*i*i,i*i*i*i,i*i*i*i*i) for i in range(11)]
print(list)

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = []
for item in countries:
    country, city = item[0]
    abbreviation = country[:3].upper()
    new_entry = [country.upper(), abbreviation, city.upper()]
    result.append(new_entry)

print(result)

# 5. Change the following list to a list of dictionaries:
for item in countries:
    
    country, city = item[0]  
    country_city_dict = {'country': country.upper(), 'city': city.upper()}
    result.append(country_city_dict)
print(result)
# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
final_names = [(final_a) for final in names for final_a in final]  
print(final_names)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1,x2,y1,y2: (x2-x1) / (y2-y1)
print(slope(2,4,4,8))