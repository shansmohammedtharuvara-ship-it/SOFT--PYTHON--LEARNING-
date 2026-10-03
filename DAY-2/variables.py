# Variables in Python

first_name = 'Shans'
last_name = 'Mohammed'
country = 'India'
city = 'Malappuram'
age = 18
is_married = False

skills = ['Python', 'HTML', 'CSS', 'Java', 'SQL']

person_info = {
    'firstname': 'Shans',
    'lastname': 'Mohammed',
    'country': 'India',
    'city': 'Malappuram',
    'course': 'BCA'
}


# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))

print('Last name:', last_name)
print('Last name length:', len(last_name))

print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)

print('Skills:', skills)
print('Person information:', person_info)


# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Shans', 'Mohammed', 'India', 18, False

print(first_name, last_name, country, age, is_married)

print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)