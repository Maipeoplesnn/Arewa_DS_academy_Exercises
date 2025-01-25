############################################################ Exercises: Level 1 ####################################################################

# 1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = ''.join(e for e in paragraph if e.isalnum() or e.isspace()).lower().split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(list(word_count.items()))

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive 
# direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
numbers = []
for word in text.split():
    if word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
        numbers.append(int(word))
    elif ',' in word:
        for num in word.split(','):
            if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
                numbers.append(int(num))

# Find the distance between the two furthest particles
min_num = min(numbers)
max_num = max(numbers)
distance = abs(max_num - min_num)

print("Point = ", numbers)
print(f"Sorted Point = , {sorted(numbers)}")
print(f"distance = {max_num} - ({min_num}) {distance}")

############################################################## Exercises: Level 2 #################################################################

# 1. Write a pattern which identifies if a string is a valid python variable
import re
import keyword

def is_valid_variable(var_name):
    if keyword.iskeyword(var_name):
        return False
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, var_name))
print(is_valid_variable('first_name'))  
print(is_valid_variable('first-name'))  
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname'))


### Exercises: Level 3

1. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_sentence = ''
for char in sentence:
    if char.isalpha() or char.isspace():
        clean_sentence += char
words = clean_sentence.lower().split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
most_frequent_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]

print("Cleaned text:", clean_sentence)
print("Three most frequent words:", most_frequent_words)