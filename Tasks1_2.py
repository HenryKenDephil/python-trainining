# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that has an array or a list(only in python)  a = [5, 10, 15, 20, 25]. 
# Make a new array/list of only the first and last elements of the given array/list above. 
# Once you learn functions,revisit this and write this code inside a function.
a=[5,10,15,20,25]
first_element=a[0]
last_element=a[4]
print([first_element,last_element])
breakpoint
# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
#solution:
#take input of a number(n) and make use of modulo (%)
n=int(input("Enter the number: "))
if (n%2)==0:
    print('n is an even number')
else:
    print('n is an odd number')
breakpoint