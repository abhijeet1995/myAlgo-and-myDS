def max_of(a,b):
    if a>b:
        return a
    else:
        return b

def subset(se,key):
    if len(se)==0 or key<0:
        return float("inf")*(-1)
    elif key==0:
        return 0
    else:
        return max_of(subset(se[:len(se)-1],key),subset(se[:len(se)-1],key-se[len(se)-1]))

se=[3,34,4,12,5,2]
key=9
if subset(se,key)==0:
    print(True)
else:
    print(False)
