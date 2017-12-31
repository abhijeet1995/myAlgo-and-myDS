try:
    n=7
    m=0
    print(m+" "+n)
    print(n/m)
    print("done calculation")
except ZeroDivisionError:
    print("An error occured due to division by zero")
finally:
    print("ohh yeah!!")
