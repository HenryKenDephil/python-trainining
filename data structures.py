#data structures include lists, set, tuple, set and dictionary.
#lists are used to highlight or list an array of items. for example
class_one_pupils= ["John", "Brenda", "Kevin", "Ivy", "Mildred", "Junior", "Tyson"]
print(class_one_pupils)
male_pupils=class_one_pupils[0],[2], [5], [6]
print(male_pupils)
#exercise
days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
M=days[0]
print(M)
M1=days[0].lower()
print(M1)
f=days[4].upper()
print(f)
#present data about Victor whose account balance is 30000ksh is 20 years old, has two siblings; james and mary, and he is located in mombasa
description=["Victor", "Mombasa", "20",["James", "Mary"], "30000"]
name=description[0]
print(name)
location=description[1]
print(location)
age=description[2]
print(age)
family=description[3]
print(family)
male_family=family[0]
print(male_family)
female_family=family[1]
print(female_family)
account_balance=description[4]
print(account_balance)
x="frog"
print(x)
print(x[2])
#iterating lists
#it helps to iterate items in a sequence as shown below
x=[7,8,3]
#sum function
x=[2,5,8,12]
print(sum(x))
print(sum(x[-2:]))
#sorting function
x="bug"
print(sorted(x))
#count function
x='hippo'
print(x.count('p'))
#index function
x='hippo'
print(x.index('p'))
#unpacking function is used to assign items in a sequence
x=['pig', 'cow', 'horse']
a='pig'
b='cow'
c='horse'
#delete function is used to delete an item in the sequence or the how sequence
x=[5,3,8,6]
del(x[1])
print(x)
#append function is used to append item at the end of the sequence or list
z=[5,3,8,6]
z.append(7)
print(z)
#extend function is used to append a list
z=[5,3,8,6]
y=[3,4,9,7]
z.extend(y)
print(z)
#insert function
q=[5,3,8,6]
q.insert(1,7)
print(q)
#pop function


