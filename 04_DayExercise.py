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