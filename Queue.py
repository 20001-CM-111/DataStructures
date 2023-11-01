import array as a
class Queue():
    def __init__(self,n):
        self.n=n
        self.queue=a.array('i',[0]*n)
        self.front=-1
        self.rear=-1
    def isEmpty(self):
        if self.front==-1 and self.rear==-1 or self.front>self.rear:
            print("Queue is empty!")
            return True
        else:
            return False
    def isFull(self):
        if self.rear==self.n-1:
            print("Queue is full!")
            return True
        else:
            return False
    def peek(self):
        if self.isEmpty():
            pass
        else:
            print(self.queue[self.rear])
    def push(self):
        if self.isFull():
            pass
        else:
            self.rear+=1
            print("Enter the element:")
            self.queue[self.rear]=int(input())
            if self.front==-1:
                self.front=0
    def pop(self):
        if self.isEmpty():
            pass
        else:
            print("The element deleted is ",self.queue[self.front])
            self.front+=1
    def display(self):
        if self.isEmpty():
            pass
        else:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=' ')
            print()
n=int(input("Enter the size of the Queue:"))
Q=Queue(n)
print("Enter the option:\n1.Push\n2.Pop\n3.Display\n4.IsEmpty\n5.IsFull\n6.Peek\n7.Exit")
while(True):
    c=int(input("Enter your choice:"))
    if c==1:Q.push()
    elif c==2:Q.pop()
    elif c==3:Q.display()
    elif c==4:
        if not Q.isEmpty():
            print("Queue is not empty!")
    elif c==5:
        if not Q.isFull():
            print("Queue is not full!")
    elif c==6:Q.peek()
    elif c==7:break
    else:print("Invalid option!")