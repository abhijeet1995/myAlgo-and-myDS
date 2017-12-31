def min_num(a,b,c):
    if a>b:
        temp=b
    else:
        temp=a
    if temp>c:
        return c
    else:
        return temp

a=((0,1,1,0,1),(1,1,0,1,0),(0,1,1,1,0),(1,1,1,1,0),(1,1,1,1,1),(0,0,0,0,0))
b=[]
for ele in a:
    b.append(list(ele))
i=1
j=1

while i<len(a):
    j=1
    while j<len(a[0]):
        if a[i][j]==1:
            b[i][j]=min_num(b[i-1][j], b[i][j-1], b[i-1][j-1])+1
            #print(b[i][j])
        else:
            b[i][j]=0
        j+=1
    i+=1
max=0

for i in range(0,len(a)):
    for j in range(0,len(a[0])):
        if b[i][j]>max:
            max=b[i][j]
            max_i=i
            max_j=j

i=0
j=0
temp=max_j
while i<max:
    j=0
    max_j=temp
    while j<max:
        print(a[max_i][max_j], end='    ')
        j+=1
        max_j-=1
    print("")
    max_i-=1
    i+=1
