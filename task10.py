# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.
def calculate_area(b,h):
    a=b*h
    return a
b=int(input("Enter base lenth: "))
h=int(input("Enter height: "))
area=calculate_area(b,h)
print(area,"cm^2")
