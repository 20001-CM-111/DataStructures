n=int(input('Enter the size of the array: '))
print('Enter ',n,' elements:')
l=list(int(input()) for i in range(n))
k=int(input("Enter the element to search:"))
for i in range(0,n-1):
    min=i
    for j in range(i+1,n):
        if l[j]<l[min]:
            min=j
    l[i],l[min]=l[min],l[i]
le=0
r=n-1
res=-1
while(le<=r):
    m=int((le+r)/2)
    if l[m]==k:
        res=m
        print("Element found at position ",m)
        break
    elif l[m]<k:
        le=m+1
    else:
        r=m-1
if res==-1:
    print("Element not found!")
