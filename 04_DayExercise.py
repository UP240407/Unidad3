#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Thirty='Thirthy'
Days='Days'
Of='of'
Python='Python'
Thirty_days_of_python=Thirty+' '+Days+' '+Of+' '+Python
print(Thirty_days_of_python)
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
A='Coding'
B='for'
C='All'
Full_text=A+' '+B+' '+C+"."
print(Full_text)
#Declare a variable named company and assign it to an initial value "Coding For All".
Company="Coding For All"
#Print the variable company using _print()_.
print(Company)
#Print the length of the company string using _len()_ method and _print()_.
print(len(Company))
#Change all the characters to uppercase letters using _upper()_ method.
Company_up=Company.upper()
print(Company_up)
#Change all the characters to lowercase letters using _lower()_ method.
Company_low=Company.lower()
print(Company_low)
#Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print(Company.capitalize())
print(Company.title())
print(Company.swapcase())
#Cut(slice) out the first word of _Coding For All_ string.
first_six = Company[0:7]
print(first_six)
next_four = Company[7:11]
print(next_four)
last_four = Company[11:14]
print(last_four)
#Check if 'Coding For All' string contains a word 'Coding' using the method index, find or other methods.
str1 = "Coding For All"
contains_coding = "Coding" in str1
#Replace the word 'Coding' in the string 'Coding For All' to 'Python'.
str2 = str1.replace("Coding", "Python")
#Change 'Python for Everyone' to 'Python for All' using the replace method or other methods.
str3 = "Python for Everyone"
str3 = str3.replace("Everyone", "All")
#Split the string 'Coding For All' using space as the separator (split()).
split_str1 = str1.split()
#Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(", ")
#What is the character at index 0 in the string 'Coding For All'?
char_at_index_0 = str1[0]
#What is the last index of the string 'Coding For All'?
last_index = len(str1) - 1
#What character is at index 10 in 'Coding For All' string?
char_at_index_10 = str1[10]
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym1 = ''.join(word[0] for word in "Python For Everyone".split())
#Create an acronym or an abbreviation for the name 'Coding For All'.
acronym2 = ''.join(word[0] for word in "Coding For All".split())
#Use index to determine the position of the first occurrence of 'C' in 'Coding For All'.
first_c_index = str1.index("C")
#Use index to determine the position of the first occurrence of 'F' in 'Coding For All'.
first_f_index = str1.index("F")
#Use rfind to determine the position of the last occurrence of 'l' in 'Coding For All People'.
str4 = "Coding For All People"
last_l_index = str4.rfind("l")
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
first_because_index = sentence.index("because")
#Use rindex to find the position of the last occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
last_because_index = sentence.rindex("because")
#Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = sentence[31:54]
#Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
first_because_index = sentence.find("because")
#Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = sentence[sentence.find("because"):sentence.rfind("because") + len("because")]
#Does 'Coding For All' start with a substring 'Coding'?
starts_with_coding = str1.startswith("Coding")
#Does 'Coding For All' end with a substring 'coding'?
ends_with_coding = str1.endswith("coding")
#Remove the left and right trailing spaces in the given string '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'.
str_with_spaces = "   Coding For All     "
trimmed_str = str_with_spaces.strip()
#Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python
identifier1 = "30DaysOfPython".isidentifier()
identifier2 = "thirty_days_of_python".isidentifier()
#The following list contains the names of some python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = " # ".join(libraries)
#se the new line escape sequence to separate the following sentences.
#     I am enjoying this challenge.
#     I just wonder what is next.
new_line_sentence = "I am enjoying this challenge.\nI just wonder what is next."
#Use a tab escape sequence to write the following lines.
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
tabbed_sentence = "Name\tAge\tCountry\tCity\nIsaac\t19\tMexico\tAguascalientes"
#Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
formatted_sentence = f"The area of a circle with radius {radius} is {area} meters square."
#Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a, b = 8, 6
addition = f"{a} + {b} = {a + b}"
subtraction = f"{a} - {b} = {a - b}"
multiplication = f"{a} * {b} = {a * b}"
division = f"{a} / {b} = {a / b:.2f}"
modulus = f"{a} % {b} = {a % b}"
floor_division = f"{a} // {b} = {a // b}"
exponentiation = f"{a} ** {b} = {a ** b}"
