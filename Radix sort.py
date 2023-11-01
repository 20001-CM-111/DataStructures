n=int(input("Enter the no of elements:"))
b=int(input("Enter the base of the elements"))
print("Enter ",n," elements:")
l=list()
for i in range(n):
    if i==0:
        max=int(input())
        l.append(max)
    else:
        l.append((int(input())))
        if l[i]>max:
            max=l[i]
c=0
while(max!=0):
    max//=10
    c+=1
buckets=[[] for i in range(b)]
for i in range(c):
    for j in range(n):
        p=l[j]%pow(10,i+1)
        p=int(p/pow(10,i))
        buckets[p].append(l[j])
    l=[]
    for k in range(b):
        l=l+buckets[k]
    buckets=buckets=[[] for i in range(b)]
print(l)
