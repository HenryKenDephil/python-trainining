#you surround a dangerous section of code with "try" and "except" if the code in the "try" works-the "except" is skipped. if the code in the "try" it skipped to the "except" section
#example
astr='hello Bob' #when the first conversion fails, it just drops into the except:clause and the program continues.
try:
    istr=int(astr)
except:
    istr=-1 #python try exept.py, First-1, Second 123
print('First', istr)
astr='123'
try:
    istr=int(astr)
except:
    istr=-1
print('Second', istr)   #when the second conversion succeeds, it just skeeps the except clause and the program continues. 
    

