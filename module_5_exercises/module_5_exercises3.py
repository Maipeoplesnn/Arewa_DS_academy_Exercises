################################################# Tuple Exercises: Level 1 #########################################################################

# 1. Create an empty tuple
tuple_var = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Binta","Amina","Bilkisu")
brothers = ("Sani","Mukhtar","Muhammad")

#3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
modify_siblings = list(siblings)
modify_siblings.append("Yunusa")
modify_siblings.append("Hauwa'u")
family_members = tuple(modify_siblings)


############################################################ Tuple Exercises: Level 2 ##########################################################

# 1. Unpack siblings and parents from family_members
a, b, c, d, e, f, g, h = family_members
print(a, b, c, d, e, f, g, h)

# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Apple", "Orange", "Watermelon")
vegetables = ("Lettuce", "Cabbage", "Carrot")
animal_products = ("Honey", "Milk", "Eggs")
food_stuff_tp = fruits + vegetables + animal_products

# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[4])

# 1. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3])
print(food_stuff_lt[6:9])

# 1. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 1. Check if an item exists in  tuple:
print(food_stuff_tp)

# -Check if 'Estonia' is a nordic country and -Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# -Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)

# -Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)