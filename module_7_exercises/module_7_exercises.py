############################################################# Exercises: Level 1 ####################################################################

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))
years = 18 - age
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {years}  more years to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
your_age = int(input("Enter your age: "))
my_age = 30
year_diff = abs(my_age - your_age)
if your_age > my_age:
    if year_diff == 1:
        print(f"You are {year_diff} year older than me.")
    else:
         print(f"You are {year_diff} years older than me.")
elif your_age < my_age:
    if year_diff == 1:
        print(f"You are {year_diff} year younger than me.")
    else:
        print(f"You are {year_diff} years younger than me.")
else:
    print(f"You are {my_age} years too 😱?, What a wonderful surprise! We're the same age!")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
first_numb = int(input("Enter first number: "))
second_numb = int(input("Enter second number: "))
if first_numb > second_numb:
    print(f"{first_numb} is greater than {second_numb}")
elif second_numb > first_numb:
    print(f"{second_numb} is greater than {first_numb}")
else:
    print(f"{first_numb} is equal to {second_numb}")

############################################################# Exercises: Level 2 ####################################################################

# 1. Write a code which gives grade to students according to theirs scores:
Mark = float(input('Enter your mark = '))
if Mark >= 70 and Mark <= 100:
    print('A')
elif Mark >= 60 and Mark < 70:
    print('B')
elif Mark >= 50 and Mark < 60:
    print('C')
elif Mark >= 45 and Mark < 50:
    print('D')
elif Mark >= 40 and Mark < 44:
    print('E')
elif Mark >= 0 and Mark <40:
        print("F")
else:
    print("invalid result")
        

# 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
season = input("Do you want check the season that each month fall in?, Type the month here: ").title()
if season == "September" or season == "October" or season == "November":
    print("the season is Autumn")
elif season == "December" or season == "January" or season == "February":
    print("the season is Winter")
elif season == "March" or season == "April" or season == "May":
    print(" the season is Spring")
elif season == "June" or season == "July" or season == "August":   
    print(" the season is Summer")
else:
    print("Invalid Input")

#2. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Type a fruit to search or add: ").lower()
if fruit in fruits:                                
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)                        
    print("Updated fruit list:", fruits)        

############################################################# Exercises: Level 3 ####################################################################

# 1. Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Abdullahi',
    'last_name': 'Yunusa',
    'age': 25,
    'country': 'Nigeria',
    'is_marred': False,
    'skills': ['JavaScript', 'HTML&CSS', 'PHP', 'SQL', 'Python'],
    'address': {
        'street': 'SGwarzo road opposite Inec Office',
        'zipcode': '02210'
    }
    }

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
person = {
    'first_name': 'Abdullahi',
    'last_name': 'Yunusa',
    'age': 25,
    'country': 'Nigeria',
    'is_marred': False,
    'skills': ['JavaScript', 'HTML&CSS', 'PHP', 'SQL', 'Python'],
    'address': {
        'street': 'SGwarzo road opposite Inec Office',
        'zipcode': '02210'
    }
    }

check = "skills" in person
if check == True:
    print(person["skills"][2])

# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
person = {
    'first_name': 'Abdullahi',
    'last_name': 'Yunusa',
    'age': 25,
    'country': 'Nigeria',
    'is_marred': False,
    'skills': ['JavaScript', 'HTML&CSS', 'PHP', 'SQL', 'Python'],
    'address': {
        'street': 'SGwarzo road opposite Inec Office',
        'zipcode': '02210'
    }
    }

check = "skills" in person
check_python = person["skills"][-1] in person['skills']
if check == True and check_python == True:
    print(person["skills"][-1])

''' * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),else print('unknown title') - for more accurate results more conditions can be nested!'''

person = {
    'first_name': 'Abdullahi',
    'last_name': 'Yunusa',
    'age': 25,
    'country': 'Nigeria',
    'is_marred': False,
    'skills': ['JavaScript', 'HTML&CSS', 'PHP', 'SQL', 'Python'],
    'address': {
        'street': 'SGwarzo road opposite Inec Office',
        'zipcode': '02210'
    }
    }
if person['skills'] == ["Node","React"]:
    print("He is a front end developer")
elif person['skills'] == ["Node", "Python", "MongoDB"]:
    print("He is a back end developer")
elif person['skills'] == ["React", "Node", "MongoDB"]:
    print("He is a full stack developer")
else:
    print("Unknown ")

# * If the person is married and if he lives in Finland, print the information in the following format:
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 25,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'HTML&CSS', 'PHP', 'SQL', 'Python'],
    'address': {
        'street': 'SGwarzo road opposite Inec Office',
        'zipcode': '02210'
    }
    }
lives_status = person["is_marred"] == True and person["country"] == "Nigeria"
if lives_status == True:
    print(f"{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married")

