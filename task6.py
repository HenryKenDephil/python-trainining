# TASK 6:Using Python Only
# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half values in one line and the last half values in one line.
# Once you learn functions,revisit this and write this code inside a function
x=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first_list=x[0:5]
second_list=x[5:]
print(first_list)
print(second_list)

 # how to save your results; create result=[], then store it by print (result. append[list or i or anything that you are printing]     
#using loops
my_list=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result1=[]
for half_list in range(1,6):
    print(half_list)
for second_half in range(6,11):
    print(second_half)

#using loops
for half_list in range (1,6):
    print(half_list)  
for second_half in range (6,11):
        print(second_half)   