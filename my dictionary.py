#dictionary is created by calibraces
person={"name":"John", "age":68, "location": "Kitale", "gender":"Male"}
g=person["gender"]
print(g)
#CONCEPT 8 QUESTIONS: DATA STRUCTURES
#Determining type of variable in  taskList using an inbuilt function
#Print KES
#Print 560
#Use a function to determine the length of taskList
#Change 987 to 789 without using an inbuilt -method or Assignment
#Change the name “John” to “Jane” .
taskList=[23,'Jane',['Lesson 23',560,{'currency':'KES'}], 987,(76,'John')]
print(type(taskList))
les=taskList[2]
print(les)
currency_type=les[2]
print(currency_type)
currency_type=['currecy', 'KES']
kes=('KES')
print(kes)
number=['Lesson 23',560,{'currency':'KES'}]
n=number[1]
print(n)
length=len(taskList)
print(length)
#Change 987 to 789 without using method or function. make use of [::-1]
#identify the location of 987 as shown below;
number_location=taskList[3]
#convert the number to string first
#use n to represent the number
n=str(number_location)
#reverse the number "nr' by introducing [::-1]
nr=int(n[::-1])
#convert the reversed number (nr) back to its original string as shown below
taskList[3]=nr
print(taskList)
#change john to jane
#identify the position of john as j
j=taskList[4]
#convert tupple() into list[] by naming it j string(js)
js=list(j)
js[1]='Jane'
taskList[4]=tuple(js)
print(taskList)


