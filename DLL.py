class Node():
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None
class DLL():
    def __init__(self):
        self.head=None
        self.tail=None
        self.len=0
    def insert(self,c):
        n=int(input("Enter the element:"))
        newNode=Node(n)
        temp = self.head
        if self.head==None:
            self.head=newNode
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
                    temp.next.prev=newNode
                    newNode.next=temp.next
                    temp.next=newNode
                    newNode.prev=temp
            if c==1:
                self.head.prev=newNode
                newNode.next=self.head
                self.head=newNode
            if c==3:
                self.tail.next=newNode
                newNode.prev=self.tail
                self.tail=newNode
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
                    temp.next.prev=temp
           if c==1:
                print('The deleted element is ',self.head.data)
                self.head=self.head.next
                self.head.prev=None
           if c==3:
                print("The deleted element is ",self.tail.data)
                self.tail=self.tail.prev
                self.tail.next=None
           self.len-=1
    def display(self,c):
        if self.head==None:
            print("List is empty")
        else:
            if c==1:
                temp=self.head
                while (temp.next != None):
                    print(temp.data, " -> ", end=' ')
                    temp = temp.next
                print(temp.data)
            else:
                temp=self.tail
                while(temp.prev!=None):
                    print(temp.data," -> ",end=' ')
                    temp=temp.prev
                print(temp.data)
    def search(self):
        if self.head == None:
            print("List is empty can't search the element.")
        else:
            n = int(input("Enter the element to search : "))
            temp = self.head
            c = 1
            while (temp != None):
                if temp.data == n:
                    print("Element found at node ", c)
                    break
                temp = temp.next
                c += 1
            if c > self.len:
                print("Element not found!")
    def count(self):
        print("There are ", self.len, " elements in the list")
DLL=DLL()
print('1.Insert\n2.Delete\n3.Display\n4.Search\n5.Count\n6.Exit')
while(True):
    c=int(input("Enter your choice:"))
    if c==1:
        print('1.Insert at beginning\n2.Insert at a position\n3.Insert at end')
        while(True):
            k = int(input("Enter the position of insertion:"))
            if k==1:
                    DLL.insert(1)
                    break
            elif k==2:
                        DLL.insert(2)
                        break
            elif k==3:
                        DLL.insert(3)
                        break
            else:print("Invalid option")
    elif c==2:
        print('1.Delete at beginning\n2.Delete at a position\n3.Delete at end')
        while (True):
            k = int(input("Enter the position of deletion:"))
            if k == 1:
                DLL.delete(1)
                break
            elif k == 2:
                DLL.delete(2)
                break
            elif k == 3:
                DLL.delete(3)
                break
            else:
                print("Invalid option")
    elif c==3:
        print('1.Display from head\n2.Display from tail')
        while(True):
            k = int(input("Enter your choice of display:"))
            if k==1:
                DLL.display(1)
                break
            elif k==2:
                DLL.display(2)
                break
            else:print("Invalid option")
    elif c==4:
        DLL.search()
    elif c==5:
        DLL.count()
    elif c==6:break
    else:print("Invalid option")