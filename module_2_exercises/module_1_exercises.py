# Exercises: Level 1
# Day 2: 30 Days of python programming

# 3. Declare a first name variable and assign a value to it
first_name = "Abdullahi"

# 4. Declare a last name variable and assign a value to it
last_name = "Yunusa"

# 5. Declare a full name variable and assign a value to it
full_name = "Abdullahi Maijamaa Yunusa"

# 6. Declare a country variable and assign a value to it
country = "Nigeria"

# 7. Declare a city variable and assign a value to it
City = "Kano"

# 8. Declare an age variable and assign a value to it
age = 25

# 9. Declare a year variable and assign a value to it
year = 2024

# 10. Declare a variable is_married and assign a value to it
is_married = False

# 11. Declare a variable is_true and assign a value to it
is_true = True

# 12. Declare a variable is_light_on and assign a value to it
is_light_on = True

# 13. Declare multiple variable on one line
higher_institution, faculty, department, level, = "Bayero University, Kano", "Computing", "Information Technology", "level 400"



# Exercises: Level 2

#1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(City))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(higher_institution))
print(type(faculty))
print(type(department))
print(type(level))

# 1. Using the _len()_ built-in function, find the length of your first name
print(len(first_name))

# 1. Compare the length of your first name and your last name
print(len(first_name) == len(last_name))

# 1. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# 1. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# 1. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# 1. Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# 1. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# 1. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# 1. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# 1. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

#1. The radius of a circle is 30 meters.
    #1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
radius = 30
area_of_circle_ = 3.14 * radius ** 2

    #2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
radius = 30
circum_of_circle_ = 2 * 3.14 * radius

    #3. Take radius as user input and calculate the area.
radius = float(input ("input radius here: "))
area_of_circle_ = 3.14 * radius ** 2

# 1. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
country = input("Enter country: ")
age = input("Enter age here: ")

# 1. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')

'''Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not'''