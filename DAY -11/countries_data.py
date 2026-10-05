```python
# ==========================================
# DAY 11 - FUNCTIONS
# ==========================================

# ------------------------------
# LEVEL 1
# ------------------------------

# 1. Add two numbers

def add_two_numbers(a, b):
    return a + b


print(add_two_numbers(10, 5))


# 2. Area of a circle

def area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius


print("Area of circle:", area_of_circle(7))


# 3. Add all numbers

def add_all_nums(*numbers):
    total = 0

    for number in numbers:
        if not isinstance(number, (int, float)):
            return "Please enter only numbers."

        total += number

    return total


print("Total:", add_all_nums(5, 10, 15, 20))
print(add_all_nums(4, 8, "hello"))


# 4. Celsius to Fahrenheit

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


print("Temperature:", convert_celsius_to_fahrenheit(25), "F")


# 5. Check season

def check_season(month):
    month = month.lower()

    if month in ["september", "october", "november"]:
        return "Autumn"
    elif month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    else:
        return "Invalid month"


print("Season:", check_season("October"))


# 6. Calculate slope

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined."

    slope = (y2 - y1) / (x2 - x1)
    return slope


print("Slope:", calculate_slope(2, 3, 6, 11))


# 7. Solve quadratic equation

import math


def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2

    elif discriminant == 0:
        root = -b / (2 * a)
        return root

    else:
        return "No real solutions."


print("Quadratic solution:", solve_quadratic_eqn(1, -5, 6))


# 8. Print list items

def print_list(items):
    for item in items:
        print(item)


my_subjects = ["Python", "HTML", "CSS", "JavaScript"]
print_list(my_subjects)


# 9. Reverse a list using a loop

def reverse_list(items):
    reversed_items = []

    for item in items:
        reversed_items.insert(0, item)

    return reversed_items


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


# 10. Capitalize list items

def capitalize_list_items(items):
    capitalized = []

    for item in items:
        capitalized.append(item.capitalize())

    return capitalized


names = ["rahul", "arun", "meera", "anjali"]
print(capitalize_list_items(names))


# 11. Add an item to a list

def add_item(items, item):
    new_list = items.copy()
    new_list.append(item)
    return new_list


food_items = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_items, "Bread"))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


# 12. Remove an item from a list

def remove_item(items, item):
    new_list = items.copy()

    if item in new_list:
        new_list.remove(item)

    return new_list


food_items = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_items, "Mango"))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


# 13. Sum of numbers

def sum_of_numbers(number):
    total = 0

    for i in range(1, number + 1):
        total += i

    return total


print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))


# 14. Sum of odd numbers

def sum_of_odds(number):
    total = 0

    for i in range(1, number + 1):
        if i % 2 != 0:
            total += i

    return total


print("Sum of odds:", sum_of_odds(10))


# 15. Sum of even numbers

def sum_of_even(number):
    total = 0

    for i in range(1, number + 1):
        if i % 2 == 0:
            total += i

    return total


print("Sum of evens:", sum_of_even(10))


# ==========================================
# LEVEL 2
# ==========================================

# 1. Count evens and odds

def evens_and_odds(number):
    even_count = 0
    odd_count = 0

    for i in range(number + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("The number of odds are", odd_count)
    print("The number of evens are", even_count)


evens_and_odds(100)


# 2. Factorial

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


print("Factorial:", factorial(5))


# 3. Check if empty

def is_empty(value):
    if len(value) == 0:
        return True
    else:
        return False


print(is_empty([]))
print(is_empty(["Python"]))


# 4. Mean

def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


# Median

def calculate_median(numbers):
    if len(numbers) == 0:
        return 0

    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[middle - 1] +
                sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]


# Mode

def calculate_mode(numbers):
    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    highest = max(counts.values())

    modes = []

    for number, count in counts.items():
        if count == highest:
            modes.append(number)

    return modes


# Range

def calculate_range(numbers):
    return max(numbers) - min(numbers)


# Variance

def calculate_variance(numbers):
    mean = calculate_mean(numbers)

    total = 0

    for number in numbers:
        total += (number - mean) ** 2

    return total / len(numbers)


# Standard deviation

def calculate_std(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5


data = [2, 4, 4, 6, 8, 8, 10]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard deviation:", calculate_std(data))


# 5. Greeting function

def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()
greet("Alice")


# 6. Show arbitrary named arguments

def show_args(**kwargs):
    details = []

    for key, value in kwargs.items():
        details.append(f"{key}: {value}")

    print("Received:", ", ".join(details))


show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")


# ==========================================
# LEVEL 3
# ==========================================

# 1. Check if a number is prime

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


print("Is 17 prime?", is_prime(17))
print("Is 20 prime?", is_prime(20))


# 2. Check if all items are unique

def are_items_unique(items):
    return len(items) == len(set(items))


print(are_items_unique([1, 2, 3, 4]))
print(are_items_unique([1, 2, 2, 4]))


# 3. Check if all items have the same data type

def same_data_type(items):
    if len(items) == 0:
        return True

    first_type = type(items[0])

    for item in items:
        if type(item) != first_type:
            return False

    return True


print(same_data_type([1, 2, 3, 4]))
print(same_data_type([1, "2", 3]))


# 4. Check if a variable name is valid

def is_valid_variable(variable_name):
    return variable_name.isidentifier()


print(is_valid_variable("student_name"))
print(is_valid_variable("123student"))


# ==========================================
# LEVEL 3 - COUNTRIES DATA
# ==========================================

# Make sure countries_data.py is in the same folder.

from countries_data import countries_data


# Most spoken languages

def most_spoken_languages(data, number=10):
    language_count = {}

    for country in data:
        for language in country["languages"]:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    language_list = []

    for language, count in language_count.items():
        language_list.append([count, language])

    language_list.sort(reverse=True)

    return language_list[:number]


print("Top 10 most spoken languages:")
print(most_spoken_languages(countries_data, 10))


# Most populated countries

def most_populated_countries(data, number=10):
    country_list = []

    for country in data:
        country_list.append({
            "country": country["name"],
            "population": country["population"]
        })

    country_list.sort(
        key=lambda x: x["population"],
        reverse=True
    )

    return country_list[:number]


print("Top 10 most populated countries:")
print(most_populated_countries(countries_data, 10))
```
