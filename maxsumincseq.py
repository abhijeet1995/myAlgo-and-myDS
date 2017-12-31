def maxsum(path):
    res=[]
    for element in path:
        res.append(element)
    for i in range(1,len(path)):
        for j in range(0,i):
            if path[i]>path[j] and res[i]<res[j]+path[i]:
                res[i]=path[i]+res[j]
    max=res[0]
    for element in res:
        if element>max:
            max=element
    return max

print(maxsum([12,15,10,11,20]))
