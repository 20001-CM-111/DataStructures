from DS.QueueSLL import Queue
class node:
    def __init__(self,val):
        self.data=val
        self.lc=self.rc=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self):
        n = int(input("Enter the element to insert : "))
        newNode = node(n)
        if not self.root:
            self.root = newNode
        else:
            temp = self.root
            while(True):
                if n==temp.data:
                    print("Element is already in tree, cannot insert")
                    break
                elif n<temp.data:
                    if not temp.lc:
                        temp.lc=newNode
                        break
                    else:
                        temp=temp.lc
                else:
                    if not temp.rc:
                        temp.rc=newNode
                        break
                    else:
                        temp=temp.rc
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
        if not self.root:
            return True
        else:
            return False
    def search(self):
        k=int(input("Enter the element to search : "))
        temp=self.root
        while(temp):
            if temp.data==k:
                return True
            elif k<temp.data:
                temp=temp.lc
            else:
                temp=temp.rc
        return False
    def height(self,root):
        if not root:
            return 0
        else:
            return max(self.height(root.lc),self.height(root.rc))+1

BT=BST()
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
            if BT.search():
                print("Element found!")
            else:
                print("Element not found!")
    elif c==4:
        if BT.isEmpty():
            print("Tree is empty!")
        else:
            k=BT.height(BT.root)
            print("The height of the tree is : ",k-1 )
    elif c==5:
        break
    else:
        print("Invalid option")



