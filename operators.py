# conditional statements include the use of NOT, AND, OR
# NOT brings True if all conditions are true while OR brings true is one condition is true.
#exercise
# Prompt the user to input the marks.
# The input should be between 0 and 100. 
# Then output the correct grade: 
marks=int(input("Enter your marks"))
if marks>=0 and marks<=100:
    if marks>79 and marks<100:
        print("A plain")
    elif marks>60 and marks<79:
        print("B Minus")
    elif marks<59 and marks>49:
        print("C minus")
    elif marks>40 and marks<49:
        print("D planin")
    else:
        print('E')
else:
    print("zero attempt")
print("Finish, Done")
breakpoint

