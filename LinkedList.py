class Node():
    def __init__(self,item):
        self.data=item
        self.next=None
class SingleLinkedList():
    def __init__(self):
        self.head=None
    def insertAtBegin(self,item):
        newnode=Node(item)
        if self.head==None:
            self.head=newnode
            print("Inserted value is ",item)
        else:
            newnode.next=self.head
            self.head=newnode
    def insertAtEnd(self,item):
        newnode=Node(item)
        if self.head==None:
            self.head=newnode
            print("Inserted value is ",item)
        else:
            p=self.head
            while p.next!=None:
                p=p.next
            p.next=newnode
            print("Inserted value is ",item)
    def insertAtPos(self,item,pos):
        newnode=Node(item)
        if self.head==None:
            self.head=newnode
            print("Inserted value is ",item)
        else:
            p=self.head
            x=p
            while x.data!=pos:
                x=p
                p=p.next
            if p==None:
                x.next=newnode
            else:
                y=x.next
                p.next=newnode
                p=p.next
                p.next=y
            print("Inserted value is ",item)
    def deleteAtBegin(self):
        if self.head==None:
            print("List is Empty")
        else:
            y=self.head.data
            x=self.head.next
            self.head=x
            print("Removed node is ",y)
            #return y
    def deleteAtEnd(self):
        if self.head==None:
            print("List is Empty")
        else:
            p=self.head
            x=p
            while p.next!=None:
                x=p
                p=p.next
            y=p.data
            x.next=None
            print("Removed node is ",y)
            #return y
    def deleteAtPos(self,pos):
        if self.head==None:
            print("List is Empty")
        else:
            p=self.head
            x=p
            while p.data!=pos:
                x=p
                p=p.next
            x.next=p.next
            print("Removed node is ",pos)
            #return y
    def display(self):
        if self.head==None:
            print("List is Empty")
        else:
            p=self.head
            while p!=None:
                print("->",p.data,end="")
                p=p.next
            print()
l=SingleLinkedList()
y=False
while not y:
    x=str(input("Enter your choice\n1.Insert at Begin\n2.Insert at end\n3.Insert at Pos\n4.Delete at begin\n5.Delete at end\6.Delete at pos\n7.Display\n8.Exit\n"))
    print(x)
    if x=="1":
        z=input("Enter the element to be inserted  ")
        l.insertAtBegin(z)

    elif x=="2":
        z=input("Enter the element to be inserted  ")
        l.insertAtEnd(z)
    elif x=="3":
        z=input("Enter the element to be inserted  ")
        s=input("After which node element has to be inserted")
        l.insertAtPos(z,s)
    elif x=="4":
        l.deleteAtBegin()
    elif x=="5":
        l.deleteAtEnd()
    elif x=="6":
        s=input("Enter the node to be deleted")
        l.deleteAtPos(s)
    elif x=="7":
        l.display()
    elif x=="8":
        y=True
