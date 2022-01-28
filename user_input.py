#we can instruct python to pause and read data from the user using the input() fucntion. the input() function returns a string
name=input("who are you?")
print("welcome", name)
breakpoint
#converting user input
#if we want to read a number from the user, we must convert it from a string to a number using a type conversion fucntion. later we will deal with bad input data. 
#build an elevator that converts the floor labels in UK to the floor labels in US. In UK, the floor label starts from 0 while it starts from 1 in the US.
floor_in_europe="euf"
floor_in_us="usf"
euf=input("Europe floor?")
usf=int(euf)+1
print("US floor",usf)
breakpoint
#using comments in python
#anyting after a # is ignored by python
#comments is used to describe what is going to happen in a sequence of code
#it documents who wrote the code or other ancillary information
#turn off a line of code-perhaps temporarily. 
x=20
if x<=15:
    print("small")
elif x>=16:
    print('medium')
else:
    print('larger')
print('Finsih, done')
    
