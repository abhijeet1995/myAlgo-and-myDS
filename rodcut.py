def max_of(a,b):
    if a>b:
        return a
    else:
        return b

def rod_cut(choose,cost,key):
    if len(choose)==0 or key<=0:
        return 0
    if choose[len(choose)-1]>key:
        return rod_cut(choose[:len(choose)-1],cost[:len(cost)-1],key)
    return max_of((rod_cut(choose[:len(choose)-1],cost[:len(cost)-1],key)),(cost[len(cost)-1]+rod_cut(choose,cost,key-cost[len(cost)-1])))

choose=[1,2]
cost=[3,4]
print(rod_cut(choose,cost,3))
