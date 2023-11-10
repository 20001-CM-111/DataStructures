n=int(input('Enter the size of the array: '))
print('Enter ',n,' elements:')
l=list(int(input()) for i in range(n))
def sort(a,l,r):
    if l<r:
        mid=int((l+r)/2)
        sort(a,l,mid)
        sort(a,mid+1,r)
        merge(a,l,mid,r)
    return a
def merge(a,l,m,r):
    b=[0]*(r+1)
    k=l
    i=l
    j=m+1
    while(i<=m and j<=r):
        if a[i]<=a[j]:
            b[k]=a[i]
            i=i+1
            k=k+1
        else:
            b[k]=a[j]
            j=j+1
            k=k+1
    while i<=m:
        b[k]=a[i]
        i=i+1
        k=k+1
    while j<=r:
        b[k]=a[j]
        j=j+1
        k=k+1
    for i in range(l,(r+1)):
        a[i]=b[i]
print(sort(l,0,n-1))
