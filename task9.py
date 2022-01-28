# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the age in years and returns the age in days.Use 365 days as the length of a year for this challenge as we would like to ignore leap years. Only accept positive numbers.
# Once you learn functions,revisit this and write this code inside a function
#let age be A
a=int(input("Enter your age in years: "))
if a>-1 and a>=1:
    print(a*int(365), "Days")
else:
    print("Invalid number, kindly insert a positive figure")