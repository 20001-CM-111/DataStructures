import math
from DS.Stk import Stack
s=input('Enter the postfix expression with spaces: ')
l=s.split(' ')
Stk=Stack(len(l))
for i in l:
    if i not in ['+','-','*','/','%','^']:
        print("Yes 1")
        Stk.push(int(i))
        print(Stk.top)
    else:
        Stk.peek()
        x=Stk.pop()
        y=Stk.pop()
        print("Yes")
        if i=='+':
            z=y+x
        elif i=='-':
            z=y-x
        elif i=='*':
            z=y*x
        elif i=='/':
            z=int(y/x)
        elif i=='%':
            z=y%x
        else:
            z=int(math.pow(y,x))
        Stk.push(z)
    x=Stk.pop()
print(x)
