def coin_change(val,st):
    if val==0:
        return 1
    elif val<0 or len(st)==0:
        return 0
    else:
        return coin_change(val,st[:len(st)-1])+coin_change(val-st[len(st)-1],st)

val=4
st=[1,2,3]
print(coin_change(val,st))
