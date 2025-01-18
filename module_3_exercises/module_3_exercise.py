# 1. Declare your age as integer variable
age = 25

# 2. Declare your height as a float variable
height = 45.65

# 3. Declare a variable that store a complex number
complex_num = 4 + 9j

''' 4.  Write a script that prompts the user to enter base and height of the triangle 
        and calculate an area of this triangle (area = 0.5 x b x h)'''
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = (0.5 * base * height)
print("The area of the triangle is ",  area_of_triangle)

''' 5.  Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
        Calculate the perimeter of the triangle (perimeter = a + b + c).'''
side_a = float(input("enter side a: "))
side_b = float(input("enter side b: "))
side_c = float(input("enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter)

''' 6.  Get length and width of a rectangle using prompt. Calculate its area (area = length x width) 
        and perimeter (perimeter = 2 x (length + width))'''
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

''' 7.  Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.'''
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
c = 2 * 3.14 * radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", c)

''' 8.  Calculate the slope, x-intercept and y-intercept of y = 2x - 2.
        from the formula y = mx + b
        to solve for x-intercept, set y = 0
        0 = mx + b
        b = mx
        x = -b/m
        where m = slope, and b = y-intercept'''

m1 = 2                           #Slope 
b = -2                      
x_intercept = -b / m1           # Calculate x-intercept
y_intercept = b                 # Calculate y-intercept
print("The slope of y = 2x - 2: ", m1)
print("The x-intercept of y = 2x - 2: ", x_intercept)
print("The y-intercept of y = 2x - 2: ", y_intercept)

'''' 9. Slope is (m = y2-y1/x2-x1). Find the slope 
    and Euclidean distance between point (2, 2) and point (6,10)
    slope formula = y2-y1/x2-x1'''
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m2 = (y2 - y1) / (x2 - x1)
print("The slope between point (2, 2) and point (6,10) is: ", m2)

euclidean = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5                                # euclidean formula = √((x2 - x1)² + (y2 - y1)²)
print("The euclidean distance between point(2, 2) and point(6, 10) is: ",euclidean)

# 10. Compare the slopes in tasks 8 and 9
print("Is slope in task 8 equal to slope in task 9 ? ", m1 is m2)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = 1                            # when x = 1, y = 16
y = x ** 2 + 6 * x + 9
print(y)

x = 0                            # when x = 0, y = 9
y = x ** 2 + 6 * x + 9
print(y)

x = -1                            # when x = -1, y = 4
y = x ** 2 + 6 * x + 9
print(y)

x = -2                            # when x = -2, y = 1
y = x ** 2 + 6 * x + 9
print(y)

x = -3                            # the value of y is going to be 0 when x = -3 
y = x ** 2 + 6 * x + 9
print(y)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_len = len("python")
dragon_len = len("dragon")
print(python_len is not dragon_len)

# 13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
python = "on" in ("python" and "dragon")
print(python)

# 14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
sentence = "jargon" in "I hope this course is not full of jargon"
print(sentence)

# 15. There is no 'on' in both dragon and python
sentence = "on" not in ("dragon" and "python")
print(sentence)

# 16. Find the length of the text _python_ and convert the value to float and convert it to string
text = str(float(len("dragon")))
print(text)

''' alternatively
text = float(len("dragon"))
print(text)
text_str = str(text)
print(text_str)'''

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python
number = int(input("enter number: "))
# using condition statement and modulo division
if number % 2 == 0:
    print(number)
elif number != 0:
    print(number)
else:
    print("Number is neither even nor odd")

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
convert = int(2.7)
print(7 // 3 == convert)

# 19. Check if type of '10' is equal to type of 10
print(type("10") is type(10))

# 20. Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

# 21.Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
pay_hour = float(input("Enter hours: "))
pay_rate = float(input("Enter rate per hour: "))
total_pay = pay_hour*pay_rate
print("Your weekly earnings is ", total_pay)

# 22.Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input("Enter number of years you have lived: "))
days_per_year = 365                     # number of days in year
days = years * days_per_year            # number of days in years lived
seconds = days * 24 * 60 * 60           # Calculate the number of seconds (60 seconds/minute * 60 minutes/hour * 24 hours/day)
print(f"You have lived for {seconds} seconds")

# 23.Write a Python script that displays the following table
rows = 6
for i in range(1, rows):
    for j in range(4):
        print(i ** j, end=' ')
    print()
