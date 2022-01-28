# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.
#let phone_number be pn
# pn=str(input("Enter your contact: "))
# print(pn[0:2])
# if pn[0:4]=="+254" or pn[0:2]=="07" or pn[0:1]=="7" or pn[0:3]=="254" or pn[0:2]=="01":
#     if pn[0:4]=="+254":
#         print("+254"+pn[4:])
#     if pn[0:2]=="07":
#         print("+254"+pn[1:])
#     if pn[0:1]=="7":
#         print("+254"+pn)
#     if pn[0:3]=="254":
#         print("+254"+pn[3:])
#     if pn[0:2]=="01":
#         print("+254"+pn[1:])    
# else:
#     print("Sorry, invalid phone number")

# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol. 
# Hint: In Python you can use the string split method e.g my_email.split(“@”) or my_email(“@” )
# Once you learn functions,revisit this and write this code inside a function.
#slipt email by "@" and give it variable at and split the second email by "." and it variable dot
# email=str(input("Enter your email: "))
# at=email.split("@")
# dot=email.split(".")
# if len(at)==2 and len(dot)==2:
#     print("congratulations, email is valid")
# else:
#     print("invalid email, kindly try again")
# breakpoint
# email="john@mail.com"
# sp=email.split("@")
# print(sp)
# print(type(sp))
# print(len(sp))
# print('@' in email)
# #alternativel:
# if '@' in email and "." in email:
#     print("Congratualtions, the email is valid")
# #ignoring email if starts with integer using "try and except"
email=input("enter email")
try:
    test=int(email[0])
    print("Invalid email")
except:
    if "@" in email and "." in email:
        print("congratulations, valid email")
    else:
        print("invalid")