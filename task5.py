# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
# Extras:
# If the number is a multiple of 4, display out a different message.
# Once you learn functions,revisit this and write this code inside a function
Jane=12
Bob=10
Winny=11
if Jane>Bob and Jane>Winny and Jane%4==0:
    print('Jane is bigger')
elif Winny<Jane and Winny>Bob:
    print('Winny is medium')
else:
    print("Bob is younger")
if Jane%4==0:
    print("Jane's age is a multiple of 4")
if Winny%4==0:
    print("Winny's age is a multiple of 4")
if Bob%4==0:
    print("Bob's age is a multiple of 4")
else:
      print()

              
                           
