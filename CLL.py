#All accessess starts from 1
class Node():
    def __init__(self,val):
        self.data=val
        self.next=None
class CLL():
    def __init__(self):
        self.head=None
        self.len=0
        self.tail=None
    def insert(self,c):
        n=int(input("Enter the element:"))
        newNode=Node(n)
        temp = self.head
        if self.head==None:
            self.head=newNode
            newNode.next=self.head
            self.tail=newNode
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
                self.tail.next=self.head
            if c==3:
                self.tail.next=newNode
                self.tail=newNode
                newNode.next=self.head
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
                self.tail.next=self.head
           if c==3:
                temp=self.head
                while(temp.next!=self.tail):
                    temp=temp.next
                print("The deleted element is ",self.tail.data)
                self.tail=temp
                temp.next=self.head
           self.len-=1
    def display(self):
        temp=self.head
        if temp==None:
            print("List is empty")
        else:
            k=int(input("Enter the starting position from which to display:"))
            for i in range(k-1):
                temp=temp.next
            l=temp
            while(temp.next!=l):
                print(temp.data," -> ",end=' ')
                temp=temp.next
            print(temp.data)
    def search(self):
        if self.head==None:
            print("List is empty can't search for an element.")
        else:
            n=int(input("Enter the element to search : "))
            temp=self.head
            c=1
            while(True):
                if  temp.data==n:
                    print("Element found at node ",c)
                    break
                temp=temp.next
                c+=1
                if temp==self.head:
                    break
            if c>self.len:
                print("Element not found!")
    def count(self):
        print("There are ",self.len," elements in the list")
CLL=CLL()
print('1.Insert\n2.Delete\n3.Display\n4.Search\n5.Count\n6.Head value\n7.Tail value\n8.Exit')
while(True):
    c=int(input("Enter your choice:"))
    if c==1:
        print('1.Insert at beginning\n2.Insert at a position\n3.Insert at end')
        while(True):
            k = int(input("Enter the position of insertion:"))
            if k==1:
                    CLL.insert(1)
                    break
            elif k==2:
                        CLL.insert(2)
                        break
            elif k==3:
                        CLL.insert(3)
                        break
            else:print("Invalid option")
    elif c==2:
        print('1.Delete at beginning\n2.Delete at a position\n3.Delete at end')
        while (True):
            k = int(input("Enter the position of deletion:"))
            if k == 1:
                CLL.delete(1)
                break
            elif k == 2:
                CLL.delete(2)
                break
            elif k == 3:
                CLL.delete(3)
                break
            else:
                print("Invalid option")
    elif c==3:
        CLL.display()
    elif c==4:
        CLL.search()
    elif c==5:
        CLL.count()
    elif c==6:print("The head value is ",CLL.head.data)
    elif c == 7:
        print("The tail value is ", CLL.tail.data)
    elif c==8:break
    else:print("Invalid option")