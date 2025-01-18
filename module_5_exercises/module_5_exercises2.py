## 💻 Sets Exercises
# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

##################################################### Sets Exercises: Level 1 #############################################################

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update("Hewlett Packerd", "Instagram", "Tik Tok")

# 4. Remove one of the companies from the set it_companies
it_companies.pop()

# 5. What is the difference between remove and discard
remove_method = "remove() : Raise an error when item not found"
discard_method = "discard() : Raise does not raise an error when item not found"

#################################################### Sets Exercises: Level 2 ###############################################################

# 1. Join A and B
A.union(B)

# 1. Find A intersection B
A.intersection(B)

# 1. Is A subset of B
A.issubset(B)

# 1. Are A and B disjoint sets
A.disjoint(B)

# 1. Join A with B and B with A
A.union(B)
B.update(A)

# 1. What is the symmetric difference between A and B
A.symmetric_difference(B)
output: {27, 28}

# 1. Delete the sets completely
del A, B

################################################### Sets Exercises: Level 3  ################################################################

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_to_set = set(age)
print(len(age_to_set) == len(age))
print(len(age_to_set)) # 5
print(len(age)) # 8, list of ages is bigger than set of ages

# 1. Explain the difference between the following data types: string, list, tuple and set
String_explanation = "string is immutable, can contain duplicate items, string support indexing  and Ordered sequence of items"
List_explanation = "list is mutable, can contain duplicate items, list support indexing and Ordered sequence of items"
tuple_explanation = "tuple is immutable, can contain duplicate items, tuple support indexing and Ordered sequence of items"
set_explanation = "set is mutable, set does not support duplication of items likewise it does not ordered sequence of items and last but not the least, set does not support indexing at all"

# 2. _I am a teacher and I love to inspire and teach people._How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
unique_word = "I am a teacher and I love to inspire and teach people."
unique_words = unique_word.split()
unique_set = set(unique_words)
print(unique_set)