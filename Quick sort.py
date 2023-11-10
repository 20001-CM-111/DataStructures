n=int(input("Enter the no of elements:"))
print("Enter ",n," elements:")
a=list(int(input()) for i in range(n))
def sort(a,l,r):
    if l<r:
        p=partition(a,l,r)
        sort(a,l,p-1)
        sort(a,p+1,r)
    return a
def partition(a,l,r):
    low=l
    p=a[l]
    l+=1
    while(l<=r):
        if a[l]<p:
            l+=1
        if  a[r]>=p:
            r-=1
        if l<=r:
            a[l],a[r]=a[r],a[l]
    a[r],a[low]=a[low],a[r]
    return r
print(sort(a,0,n-1))