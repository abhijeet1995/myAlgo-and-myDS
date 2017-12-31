def min_of(a,b,c):
    if a>b:
        if b>c:
            return c
        else:
            return b
    else:
        if a>c:
            return c
        else:
            return a

def find_path(a,i,j):
    if i>=len(a) or j>=len(a[0]):
        return float('inf')
    elif i==len(a)-1 and j==len(a[0])-1:
        return a[i][j]
    else:
        return a[i][j]+min_of(find_path(a,i+1,j),find_path(a,i,j+1),find_path(a,i+1,j+1))

a=[[1,2,3],[4,8,2],[1,5,3]]
print(find_path(a,0,0))
