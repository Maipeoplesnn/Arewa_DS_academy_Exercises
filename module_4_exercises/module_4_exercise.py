# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
'''string1 = "Thirty"
string2 = "Days"
string3 = "Of"
string4 = "Python"
print(f'{string1} {string2} {string3} {string4}')'''

string1 = ["Thirty", "Days", "Of", "Python"]
string2 = ' '.join(string1)
print(string2)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_code = ["Coding", "For", "All"]
string_code1  = ' '.join(string_code)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company =  "Coding For All"

# 4. Print the variable company using _print()_.
print(company)

# 5. Print the length of the company string using _len()_ method and _print()_.
print(len(company))

# 6. Change all the characters to uppercase letters using _upper()_ method.
print(company.upper())

# 7. Change all the characters to lowercase letters using _lower()_ method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of _Coding For All_ string.
print(company[:6])

# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print(company.count("Coding"))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
string_everyone = "Python For Everyone"
print(string_everyone.replace("Everyone", "All"))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
softwares = "Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon"
print(softwares.split(","))

# 15. What is the character at index 0 in the string _Coding For All_.
print(company[:1]) # company[0], company[0:1] 

# 16. What is the last index of the string _Coding For All_.
sub_string =  "l"
print(company.rindex(sub_string))

# 17. What character is at index 10 in "Coding For All" string.
print(company[10:11])     #company = "Coding For All"

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
print(' '.join(string_everyone.upper() for string_everyone in company))

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
print(' '.join(company[0].upper() for company in company.split(' ')))

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
new_name = company.lower()
print(new_name.find('c'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
find_l = "Coding for All People"
print(find_l.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' '''
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[31:54])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rindex('because'))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[31:54])

# 28. Does '\'Coding For All' start with a substring _Coding_?
No

# 29. Does 'Coding For All' end with a substring _coding_?
No

# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
string = "      Codings For All         "
print(string.strip("        "))
      
# 31. Which one of the following variables return True when we use the method isidentifier():
- thirty_days_of_python

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib = ['Django', 'Flask', 'Pyramid', 'Falcon']
print('# '.join(lib))

# 33. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Use a tab escape sequence to write the following lines.
print("Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki")

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square")

# 36. Make the following using string formatting methods:
a = 8
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
