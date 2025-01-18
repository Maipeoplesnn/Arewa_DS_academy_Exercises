# Exercises: Level 1

# 1. Declare an empty list
my_list = []

# 2. Declare a list with more than 5 items
my_list = [1, "Two", 3.0, "Four", 5]

# 3. Find the length of your list
print(len(my_list))

# 4. Get the first item, the middle item and the last item of the list
print(my_list[::2])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
my_new_list = ["Abdullahi Maijamaa Yunusa", 25, 42.4,"single", "Galadimawa Shanono, opposite INEC office"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using _print()_
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[::3])

# 10. Print the list after modifying one of the companies
it_companies[0] = "WhatsApp"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("IT")

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4, "IT")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = "FACEBOOK"

# 14. Join the it_companies with a string '#;&nbsp; '
print("# ".join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
check = "Facebook" in it_companies

# 16. Sort the list using sort() method
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies from the 
print(it_companies[3:4])

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
it_companies.pop(3)

# 23. Remove the last IT company from the list
it_companies.pop()

# 24. Remove all IT companies from the list
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_company = front_end + back_end

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
'''full_stack = front_end + back_end
full_stack.insert(5, ['python','SQL'])
full_stack'''

full_stack = front_end + back_end
full_stack.insert(5, "python")
full_stack.insert(5, "SQL")

# Exercises: Level 2

#1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age
ages.sort()                    # 19, 19, 20, 22, 24, 24, 24, 25, 25, 26
minimum = min(ages[:])
maximum = max(ages[:])           
print(minimum)                  # min = 19
print(maximum)                  #max = 26

# - Add the min age and the max age again to the list
ages.append(minimum)
ages.append(maximum)

# - Find the median age (one middle item or two middle items divided by two)
ages.sort()         #list items = 12
print((ages[5] + ages[6])/len(ages[5:7]))

# - Find the average age (sum of all items divided by their number)
average = (sum(ages[:])/len(ages))           
print(average) 

# - Find the range of the ages (max minus min)
ages.sort()
rng = max(ages[:]) - min(ages[:])
print(rng)

# - Compare the value of (min - average) and (max - average), use _abs()_ method
ages = [19, 19, 22, 19, 24, 20, 25, 26, 24, 25, 24,26]
average = (sum(ages[:])/len(ages))
abs(min(ages[:]) - average) == abs(max(ages[:]) - average)

# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
middle_countries = [len(countries)//2]
print(middle_countries)

# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(countries[0:97])
print(countries[97::])

# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
f_three = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_countries, second_countries, third_countries, *scandic = f_three
print(first_countries)
print(second_countries)
print(third_countries)
print(scandic)