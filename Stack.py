import array as a
class Stack():
    def __init__(self,n):
        self.n=n
        self.Stk=a.array('i',[0]*n)
        self.top=-1
    def isEmpty(self):
        if self.top==-1:
            print("DS is empty!")
            return True
        else:
            return False
    def isFull(self):
        if self.top==self.n-1:
            print("DS is full!")
            return True
        else:
            return False
    def peek(self):
        if self.isEmpty():
            pass
        else:
            print(self.Stk[self.top])
    def push(self):
        if self.isFull():
            pass
        else:
            self.top+=1
            print("Enter the element:")
            self.Stk[self.top]=int(input())
    def pop(self):
        if self.isEmpty():
            pass
        else:
            print("The element deleted is ",self.Stk[self.top])
            self.top-=1
    def display(self):
        if self.isEmpty():
            pass
        else:
            for i in range(self.top,-1,-1):
                print(self.Stk[i])
n=int(input("Enter the size of the stack:"))
Stk=Stack(n)
print("Enter the option:\n1.Push\n2.Pop\n3.Display\n4.IsEmpty\n5.IsFull\n6.Peek\n7.Exit")
while(True):
    c=int(input("Enter your choice:"))
    if c==1:Stk.push()
    elif c==2:Stk.pop()
    elif c==3:Stk.display()
    elif c==4:
        if not Stk.isEmpty():
            print("DS is not empty!")
    elif c==5:
        if not Stk.isFull():
            print("DS is not full!")
    elif c==6:Stk.peek()
    elif c==7:break
    else:print("Invalid option!")