
"""TASK 8: Using Python or PHP or Java or Ruby or JavaScript
Write a program that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
Once you learn functions,revisit this and write this code inside a function."""
#let student marks to be m
m=int(input("Enter your marks: "))
if m>0 and m<=100:
    if m>79 and m<=100:
        print(m, "A Plain")
    elif m>60 and m<=79:
        print(m, "B Minus")
    elif m>49 and m<=59:
        print(m, "C Minus")
    elif m>40 and m<=49:
        print(m, "D Plain")
    else:
        print(m, "E")
else:
    print("Invalid, please try again")
#using functions
#marks is denoted by paremeter "m" and grade is denoted by parameter "g"
def student_score(m,g):
    m=int(input("Enter your marks"))
    print(m,g)
    if m>0 and m<=100:
        if 
