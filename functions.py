#functions make the coding be easier. examples; int(),str
#define function first and then use it.
#a function is reusable, it modularize(segments)
#the variables inside a fucntion like n1 and n2 are called parameters while values like 20 are called arguments.
#example
# def calculate():
#     t=25+30
#     print(t)
# calculate()
# def calculate(n1,n2):
#     t=n1+n2
#     return t
# x=calculate(25,30)
# print(x)
# y=calculate(68,89)
# print(y)
#creating input
# def calculate(n1,n2):
#     t=n1+n2
#     return t
# n1=int(input("enter numer1"))
# n2=int(input("enter number2"))
# x=calculate(n1,n2)
# print(x)
#a class is group of functions.
#a function does a specific task.
#read classes and objects/object oriented programming
#a function takes in data, process it and return output/results
#first define the function with data in and out
#the we use the function
#designing a calculator
def calculator():
    t=45+70
    print(t)
calculator()
#making a function reusable
def calulator(num1, num2, num3):
    t=num1 + num2 + num3
    return t
#can only return a str, boolean, tuple, set, int, dictionary,float, list, dictionar, integer, float
#variable is called as parameter in a function
#value is refered to as argument
res=calculator(34,90,67)
print(res)
#how to import
