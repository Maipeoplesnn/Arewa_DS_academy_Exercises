### Exercises: Level 1

# 1. Iterate 0 to 10 using for loop.
for num in range(0, 10):
   print(num)

# do the same using while loop.
i = 0
while i <= 10:
   print(i)
   i += 1

# 2. Iterate 10 to 0 using for loop, 
for num in range(10, -1, -1):          # for num in reversed(range(11)):
   print(num)

# do the same using while loop.
i = 10
while i >= 0:
   print(i)
   i -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(8):
    print("#" * i)

# 4. Use nested loops to create the following:
for i in range(9):
   print("# " * 8)
   
# 5. Print the following pattern:
for i in range(11):
   print(f"{i} * {i} = {i}")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lists = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lists in lists:
    print(lists)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for num in range(0, 101, 2):
   print(num)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range(1, 101, 2):
   print(num)

##################################################### Exercises: Level 2 ##########################################################################
    
# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for num in range(1, 101):
   sum += num
print(f"The sum of all numbers is {sum}")

# 1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even = 0
odd = 0
for num in range(1, 101):
    if num % 2 == 0:
        even += num
    else:
        odd += num
print(f"The sum of all evens is {even}. And The sum of all odds is {odd}")

######################################################## Exercises: Level 3 ########################################################################

# 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
# 1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
copy_list = ['banana', 'orange', 'mango', 'lemon']
for i in reversed(copy_list):
    print(i)

'''
copy_list = ['banana', 'orange', 'mango', 'lemon']
for i in copy_list[::-1]:
    print(i)
'''

# 2. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
   #1. What are the total number of languages in the data
   #2. Find the ten most spoken languages from the data
   #3. Find the 10 most populated countries in the world