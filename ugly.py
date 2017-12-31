def min(a,b,c):
    if a<b:
        temp=a
    else:
        temp=b
    if temp<c:
        return temp
    else:
        return c

ugly=[]
ugly.append(1)
i2=0
i3=0
i5=0
nmo2=2
nmo3=3
nmo5=5
for i in range(0,150):
    ugly.append(min(ugly[i2]*2,ugly[i3]*3,ugly[i5]*5))
    if ugly[i+1]==nmo2:
        i2+=1
        nmo2=2*ugly[i2]
    if ugly[i+1]==nmo3:
        i3+=1
        nmo3=3*ugly[i3]
    if ugly[i+1]==nmo5:
        i5+=1
        nmo5=5*ugly[i5]
print(ugly[i])
