#if, elif and else statements
temp=35
if temp>30:
    print("it's warm")
    print("drink water")
print("done")
#alternatively:
temp=25
if temp>30:
    print("it's warm")
    print("drink water")
elif temp>20:
    print("it's nice")
else:
    print("it's cold")
print("done")
#Ternary operator(how to write cleaner codes)
age=22
if age>=18:
    print("eligible")
else:
    print("not eligible")
#alternatively;
age=22
message="Eligible" if age >=18 else "Not Eligible"
print(message)
#operators: and, or, not. apply these operators to build an application for applying loans.
x=input("enter high_income")
x1=str(x)
y=input("enter good_crredit")
y1=str(y)
z=input("enter age")
z1=int(z)
if x1 and y1 and z1>=18:
    print("Eligible")
else: 
    enter=input("low_income" and "bad_credit" and age<=18)
    print("Not Eligible")
breakpoint
#Shadrack's way
#Eligible for loans
""" age = int(input("Enter age:"))
income = int(input("How much do you earn:"))
credit_score = int(input("What is your credit score:"))

# Eligibility 
# High income => 30000
# Age => 18
# credit_score >= 3.5

if age >= 18 and income >= 30000 and credit_score >= 3:
    print("Your are Eligible")
else:
    print("Kindly come next time") """