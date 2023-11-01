class Node():
    def __init__(self,val):
        self.data=val
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
        self.len=0
    def insert(self,c):
        n=int(input("Enter the element:"))
        newNode=Node(n)
        temp = self.head
        if self.head==None:
            self.head=newNode
        else:
            if c==2:
                p=int(input("Enter the position to insert:"))
                if p>self.len:
                    c=3
                elif p==0:
                    c=1
                else:
                    for i in range(p-2):
                        temp=temp.next
                    newNode.next=temp.next
                    temp.next=newNode
            if c==1:
                newNode.next=self.head
                self.head=newNode
            if c==3:
                while (temp.next != None):
                    temp = temp.next
                temp.next = newNode
                newNode.next = None
            self.len+=1
    def delete(self,c):
       if self.len==0:
           print("List is empty")
       else:
           temp=self.head
           if c==2:
                p = int(input("Enter the position to delete:"))
                if p>self.len:
                    c=3
                elif p==0:
                    c=1
                else:
                    for i in range(p - 2):
                        temp = temp.next
                    print("The deleted element is ", temp.next.data)
                    temp.next=temp.next.next
           if c==1:
                print('The deleted element is ',self.head.data)
                self.head=self.head.next
           if c==3:
                temp=self.head
                while(temp.next.next!=None):
                    temp=temp.next
                print("The deleted element is ",temp.next.data)
                temp.next=None
           self.len-=1
    def display(self):
        temp=self.head
        if temp==None:
            print("List is empty")
        else:
            while(temp.next!=None):
                print(temp.data," -> ",end=' ')
                temp=temp.next
            print(temp.data)
    def search(self):
        if self.head==None:
            print("List is empty can't search the element.")
        else:
            n=int(input("Enter the element to search : "))
            temp=self.head
            c=1
            while(temp!=None):
                if  temp.data==n:
                    print("Element found at node ",c)
                    break
                temp=temp.next
                c+=1
            if c>self.len:
                print("Element not found!")
    def count(self):
        print("There are ",self.len," elements in the list")
SLL=LinkedList()
print('1.Insert\n2.Delete\n3.Display\n4.Search\n5.Count\n6.Exit')
while(True):
    c=int(input("Enter your choice:"))
    if c==1:
        print('1.Insert at beginning\n2.Insert at a position\n3.Insert at end')
        while(True):
            k = int(input("Enter the position of insertion:"))
            if k==1:
                    SLL.insert(1)
                    break
            elif k==2:
                        SLL.insert(2)
                        break
            elif k==3:
                        SLL.insert(3)
                        break
            else:print("Invalid option")
    elif c==2:
        print('1.Delete at beginning\n2.Delete at a position\n3.Delete at end')
        while (True):
            k = int(input("Enter the position of deletion:"))
            if k == 1:
                SLL.delete(1)
                break
            elif k == 2:
                SLL.delete(2)
                break
            elif k == 3:
                SLL.delete(3)
                break
            else:
                print("Invalid option")
    elif c==3:
        SLL.display()
    elif c==4:
        SLL.search()
    elif c==5:
        SLL.count()
    elif c==6:break
    else:print("Invalid option")