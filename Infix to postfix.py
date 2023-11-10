from DS.Stk import Stack
s=input('Enter the infix expression: ')
res=''
Stk=Stack(len(s))
for i in s:
    if i not in ['+','-','*','/','%','^','(',')']:
        res=res+i
    else:
        if Stk.isEmpty():
            Stk.push(i)
        else:
            if i=="(":
                Stk.push(i)
            elif i==")":
                while True:
                    if Stk.peek()=='(':
                        break
                    x=Stk.pop()
                    res=res+x
                x=Stk.pop()
            elif i=="+" or i=="-":
                while True:
                    if Stk.peek()=='(' or Stk.isEmpty()==True:
                        break
                    x=Stk.pop()
                    res = res + x
                Stk.push(i)
            elif i in ["*","/","%"]:
                if Stk.peek() in ["*","/","%","^"]:
                    while True:
                        if Stk.peek() == "+" or Stk.peek() == "-" or Stk.peek() == "(" or Stk.isEmpty() == True:
                            break
                        x=Stk.pop()
                        res = res + x
                    Stk.push(i)
            else:
                if Stk.peek()=='^':
                    while True:
                        if Stk.peek() == "+" or Stk.peek() == "-" or Stk.peek() == "(" or Stk.peek() == "*" or Stk.peek() =="%" or Stk.peek() == "/" or Stk.isEmpty() == True:
                            break
                        x=Stk.pop()
                        res = res + x
                    Stk.push(i)
for i in range(Stk.top,-1,-1):
    x=Stk.pop()
    res=res+x
print('Postfix Expression: ',res)