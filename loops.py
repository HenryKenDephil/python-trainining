#loops are used to iterate elements in a list or tupes. for example, finding the elements between 1 to 100.
a=["banana", "apple", "orange", "Mangoes"]
print(a)
#using loops
#for loops
# for loops may use i to represent index
for elements in a:
    print(elements)
b=[20, 10, 5]
for i in b:
    print(i)
# find the total of b
# create another variable to hold total called sum
sum=0
for i in b:
    sum=sum+i
    print(sum)
#USING RANGE FUNCTION
#example, find the sum of 1,2,3,4
range(1,5)
#convert it to list by introducing list fucntion
d=list(range(1,5))
print(d)
for i in range(1,5):
    print(i)
#finding sum, introduce the variable tota
total=0
for i in range(1,5):
    total=total+i
    print(total)
#alternatively
total2=0
for i in range(1,5):
    total2+=i
    print(total2)
# display a multiple of 3 in (1,8)
# total3=0
# for i in range(1,8):
#     if i % 3==0:
#         print(i)
#         total3 +=i
#     print(total3)
# compute all multiples of 3 and 5 in that are less than 100
print (list(range(1,100)))
total4=0
for i in range (1,100):
    if i%3==0 or i%5==0:
        print(i)
        total4 +=i
print(total4)
#While loops
#it's more of the if function. 
#find the total of 1,2,3,4
#it uses j instead of i
total5=0
j=1
while j<5:
    print(j)
    total5 +=j
    j +=1
    print(total5)
#while loops is used when one doesnt know the number of loops available
given_list=[5,4,4,3,1,-2,-3,-5]
#find the sum of only positive numbers
total6=0
j=0
while given_list[j]>0:
    total6 +=given_list[j]
    j +=1
print(total6)
# the above method works only if we have negative numbers
#how to solve positive numbers
total7=0
j=0
while j<len(given_list) and given_list[j]>0:
    total7 +=given_list[j]
    j +=1
print(total7)
#break statements in for loops
x=[5,4,4,3,1,-2,-3,-5]
#find the sum of all elements in x and break as soon as you see a negative number in  the list
total8=0
for i in x:
    total8 +=i
    print(total8)
    total8 +=i
    if i<=0:
        break
    print(i)
print(total8)
#break statement in while loops
y=[5,4,4,3,1,-2,-3,-5]
total_y=0
i=0
while True:
    total_y +=y[i]
    i +=1
    if y[i]<=0:
        break
print(total_y)
#notes;
#for j in range(i+1)
#i=0, j=0
#i=1, j=0