############################################################# Exercises: Module 6 ####################################################################

# 1. Create  an empty dictionary called dog
dog = dict()

# 2. Add name, color, breed, legs, age to the dog dictionary
# dog.update({"name": 'Poppy',"color":"Brown","breed":"Africanis","legs":"Short","age":"3 years"})
dog["name"] = "Poppy"
dog["color"] = "Brown"
dog["breed"] = "Africanis"
dog["legs"] = "Short"
dog["age"] = "3 years"

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student["first_name"] = "Abdulalhi"
student["last_name"] = "Yunusa"
student["gender"] = "Male"
student["age"] = "25 years"
student["marital status"] = "Single"
student["skills"] = "Data analyst"
student["country"] = "Nigeria"
student["city"] = "Kano"
student["address"] = "Bayero University, Knao"

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(type(list(student['skills'])))

# 6. Modify the skills values by adding one or two skills
student["skills"] = ["Data analyst","Programmer","System Administrator"]

# 7. Get the dictionary keys as a list
keys = student.keys()

# 8. Get the dictionary values as a list
values = student.values()

# 9. Change the dictionary to a list of tuples using _items()_ method
student_list  = student.items()
print(student_list)

# 10. Delete one of the items in the dictionary
student.pop("last_name")

# 11. Delete one of the dictionaries
del student_list