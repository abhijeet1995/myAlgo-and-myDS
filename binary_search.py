def binary_search(lis, start, end, target):
    mid=(start+end)//2
    if start>end:
        return -1
    if lis[mid]==target:
        return mid
    elif lis[mid]>target:
        return binary_search(lis,start,mid-1,target)
    else:
        return binary_search(lis,mid+1,end,target)
"""
lis=[]
n=input('enter no of elements\n')
n=int(n)
for i in range(0,n):
    temp=int(input('enter element '+str(i)+'\n'))
    lis.append(temp)
target=input('enter target\n')
target=int(target)
temp=binary_search(lis,0,n-1,target)
if temp==-1:
    print('not found')
else:
    print('At index '+str(temp))
"""
