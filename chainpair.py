def chain_pair(chain):
    res=[1]*len(chain)

    for i in range(1,len(chain)):
        for j in range(0,i):
            if chain[i][0]>chain[j][1] and res[i]<res[j]+1:
                res[i]=res[j]+1

    print(res)

chain_pair([ [5, 24], [15, 25],[27, 40], [50, 60]])
