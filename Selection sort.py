n=int(input("Enter the no of elements:"))
print("Enter ",n," elements:")
l=list(int(input()) for i in range(n))
min=0
for i in range(0,n-1):
    min=i
    for j in range(i+1,n):
        if l[j]<l[min]:
            min=j
    l[i],l[min]=l[min],l[i]
    print(l)
print(l)

