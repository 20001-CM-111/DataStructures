from DS.QueueSLL import Queue
class node:
    def __init__(self,val):
        self.data=val
        self.lc=self.rc=None
class BT:
    def __init__(self):
        self.root=None
        self.Q=Queue()
    def insert(self):
        n=int(input("Enter the element to insert : "))
        newNode=node(n)
        if not self.root:
            self.root=newNode
            self.Q.insert(self.root)
        else:
            while(True):
                temp = self.Q.front
                if not temp.data.lc:
                    temp.data.lc=newNode
                    break
                elif not temp.data.rc:
                    temp.data.rc=newNode
                    break
                else:
                    self.Q.insert(temp.data.lc)
                    self.Q.insert(temp.data.rc)
                    self.Q.front=self.Q.front.next
    def display(self,c,root):
        temp=root
        if self.root==None:
            print("Tree is empty!")
        elif c==1:
            if temp:
                self.display(c,temp.lc)
                print(temp.data,end=' ')
                self.display(c,temp.rc)
        elif c==2:
            if temp:
                print(temp.data,end=' ')
                self.display(c,temp.lc)
                self.display(c,temp.rc)
        elif c==3:
            if temp:
                self.display(c,temp.lc)
                self.display(c,temp.rc)
                print(temp.data,end=' ')
        else:
            temp=self.Q.head
            while(temp):
                print(temp.data.data,end=' ')
                temp=temp.next
            temp=self.Q.front.data
            if temp.lc:
                print(temp.lc.data, end=' ')
                if temp.rc:
                    print(temp.rc.data, end=' ')
    def isEmpty(self):
        if self.root:
            return False
        else:
            return True
    def search(self,k,root):
        temp=root
        if temp:
            if temp.data==k:
                return True
            elif self.search(k, temp.lc):
                return True
            elif self.search(k, temp.rc):
                return True
        return False
    def height(self):
        c=0
        temp=self.root
        while(temp.lc):
            c+=1
            temp=temp.lc
        print("The height of the tree is : ",c)
BT=BT()
print("1.Insert\n2.Display\n3.Search\n4.Height\n5.Exit")
while(True):
    c=int(input("Enter your choice: "))
    if c==1:
        BT.insert()
    elif c==2:
        print("1.In-oder\n2.Pre-order\n3.Post-order\n4.Level-order")
        while (True):
            k = int(input("Enter your choice: "))
            if k>=1 and k<=4:
                BT.display(k,BT.root)
                print()
                break
            else:print("Invalid option!")
    elif c==3:
        if BT.isEmpty():
            print("Tree is empty, can't search an element!")
        else:
            k=int(input("Enter the element to search : "))
            if BT.search(k,BT.root):
                print("Element found!")
            else:
                print("Element not found!")
    elif c==4:
        if BT.isEmpty():
            print("Tree is empty!")
        else:
            BT.height()
    elif c==5:
        break
    else:
        print("Invalid option")


