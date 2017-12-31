a=[10,15,12,13,20,11,14,16,18,19,25]
b=[1]*len(a)
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]>a[i] and b[i]+1>b[j]:
            b[j]+=1
        #print(b) 
max=b[0]
for element in b:
    if element>max:
        max=element
print(max)
