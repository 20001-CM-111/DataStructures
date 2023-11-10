n=int(input('Enter the size of the array: '))
print('Enter ',n,' elements:')
l=list(int(input()) for i in range(n))
k=int(input("Enter the element to search:"))
c=0
for i in range(n):
    if l[i]==k:
        c=-1
        break
if c==-1:
    print("Element found at index ",i)
else:
    print("Element not found")