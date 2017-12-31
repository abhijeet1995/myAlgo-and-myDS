def min_of(a,b,c):
    if a>b:
        if c>b:
            return b
        else:
            return c
    else:
        if c>a:
            return a
        else:
            return c


def min_edit(a,b):
    if len(a)==0:
        return len(b)
    elif len(b)==0:
        return len(a)
    elif a[len(a)-1]==b[len(b)-1]:
        return min_edit(a[:len(a)-1],b[:len(b)-1])
    else:
        return min_of(1+min_edit(a[:len(a)-1],b),1+min_edit(a,b[:len(b)-1]),1+min_edit(a[:len(a)-1],b[:len(b)-1]))

a='sunday'
b='saturday'
print(min_edit(b,a))
