# Declare an empty list
empty_list = list()
# Declare a list with more than 5 items
states_of_mexico = ['Aguascalientes', 'Guadalajara', 'Chihuahua', 'Zacatecas','Sinaloa','Campeche']
# Find the length of your list
print('Number of states:', len(states_of_mexico))
# Get the first item, the middle item and the last item of the list
states_of_mexico = ['Aguascalientes', 'Guadalajara', 'Chihuahua', 'Zacatecas','Sinaloa','Campeche']
first_state = states_of_mexico[0] 
print(first_state)      
second_statet = states_of_mexico[1]
print(second_statet)     
last_state = states_of_mexico[5]
print(last_state)
last_index = len(states_of_mexico) - 1
last_state = states_of_mexico[last_index]
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Isaac','19','170','Not married','Jesus Consuelo 1517']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
# Print the list using _print()_
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
first=it_companies[0]
middle=it_companies[3]
last=it_companies[6]
# Print the list after modifying one of the companies
print(first)
print(middle)
print(last)
# Add an IT company to it_companies
it_companies.append('Tesla')
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Nissan')
print(it_companies)
#Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[1].upper())
print(it_companies[2].upper())
print(it_companies[3].upper())
print(it_companies[4].upper())
print(it_companies[6].upper())
#Join the it_companies with a string '#; '
joined_companies = " #; ".join(it_companies)
print(joined_companies)
#Check if a certain company exists in the it_companies list.
facebook_chek = "Facebook" in it_companies
print(facebook_chek)
#Sort the list using sort() method
it_companies.sort()
print(it_companies)
#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies)
# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print(last_three_companies)
#Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:  # Even number of companies
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:  # Odd number of companies
    middle_companies = [it_companies[middle_index]]
print(middle_companies)
#Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
#Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:  
    it_companies.pop(middle_index)
    it_companies.pop(middle_index - 1)
else: 
    it_companies.pop(middle_index)
print(it_companies)
#Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)
#Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#Destroy the IT companies list
del it_companies
#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
#After joining the lists in question 26, copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack_copy = full_stack.copy()
full_stack_copy.insert(full_stack_copy.index('Redux') + 1, 'Python')
full_stack_copy.insert(full_stack_copy.index('Python') + 1, 'SQL')
print(full_stack_copy)

#Exercises: Level 2

#students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Min age: {min_age}, Max age: {max_age}")
# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median_age = ages[n // 2]
print(f"Median age: {median_age}")

# Find the average age (sum of all items divided by their number)
average_age = sum(ages) / n
print(f"Average age: {average_age}")

# Find the range of the ages (max minus min)
age_range = max_age - min_age
print(f"Range of ages: {age_range}")

# Compare the value of (min - average) and (max - average), use abs() method
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
print(f"Min - Average: {min_average_diff}, Max - Average: {max_average_diff}")

# 2. Find the middle country(ies) in the countries list
countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
middle_index = len(countries) // 2
if len(countries) % 2 == 0:  # Even number of countries
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:  # Odd number of countries
    middle_countries = [countries[middle_index]]
print(middle_countries)
# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half_countries = countries[:(len(countries) + 1) // 2]
second_half_countries = countries[(len(countries) + 1) // 2:]
print(first_half_countries)
print(second_half_countries)
# 4. Unpack the first three countries and the rest as scandic countries.
first, second, third, *scandic_countries = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
print(first, second, third)
print(scandic_countries)