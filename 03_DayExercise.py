import math

# 1. Declare age as an integer
age = 19

# 2. Declare height as a float
height = 1.70

# 3. Declare a variable that stores a complex number
complex_num = 2 + 3j

# 4. Calculate the area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# 5. Calculate the perimeter of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

# 6. Calculate area and perimeter of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print(f"The area of the rectangle is {rectangle_area}")
print(f"The perimeter of the rectangle is {rectangle_perimeter}")

# 7. Calculate area and circumference of a circle
radius = float(input("Enter radius: "))
pi = 3.14
circle_area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"The area of the circle is {circle_area}")
print(f"The circumference of the circle is {circumference}")

# 8. Slope, x-intercept, and y-intercept of y = 2x - 2
m = 2
x_intercept = 2 / 2
y_intercept = -2
print(f"Slope: {m}, X-intercept: {x_intercept}, Y-intercept: {y_intercept}")

# 9. Slope and Euclidean distance between (2,2) and (6,10)
x1, y1, x2, y2 = 2, 2, 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Slope: {slope}, Distance: {distance}")

# 10. Compare slopes
print("Slopes are equal" if m == slope else "Slopes are different")

# 11. Find x where y = x^2 + 6x + 9 equals 0
for x in range(-10, 10):
    if x**2 + 6*x + 9 == 0:
        print(f"y is 0 when x = {x}")

# 12. Length comparison
print(len("python") != len("dragon"))

# 13. 'on' in 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

# 14. Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

# 15. No 'on' in both words
print("on" not in "python" and "on" not in "dragon")

# 16. Convert length of 'python' to float and string
length_python = len("python")
length_float = float(length_python)
length_str = str(length_float)
print(length_str)

# 17. Check if a number is even
num = int(input("Enter a number: "))
print(f"{num} is even: {num % 2 == 0}")

# 18. Floor division check
print(7 // 3 == int(2.7))

# 19. Type comparison
print(type("10") == type(10))

# 20. Convert '9.8' to int and check if equal to 10
try:
    print(int(float('9.8')) == 10)
except ValueError:
    print("Cannot convert '9.8' to int directly")

# 21. Calculate weekly earning
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print(f"Your weekly earning is {pay}")

# 22. Calculate seconds lived
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

# 23. Display the table
print("1 1 1 1 1")
for i in range(2, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")
