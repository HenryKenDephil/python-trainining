# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that displays all prime numbers between 1 and 200.
# Hint: A prime number is a number that is divisible by either 1 and itself.
# Once you learn functions,revisit this and write this code inside a function
#Python Program to print Prime Numbers from 1 to 200 using for loop
for number in range (1,200):
    count=0
    for i in range(2,(number//2+1)):
        if(number % i==0):
            count=count+1
            break
    if(count==0 and number!=1):
        print( number, end= " ")
#Python Program to print Prime Numbers from 1 to 200 using while loop




