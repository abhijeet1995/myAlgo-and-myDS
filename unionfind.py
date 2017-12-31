def find(i,check):
    if check[i]==-1:
        return i
    else:
        while check[check[i]]!=-1:
            i=check[i]
        return check[i]

def union(i,j,check):
    check[i]=j
    return check

def unionfind(graph):
    flag=False
    check=[-1]*len(graph)
    for i in range(0,len(graph)):
        for j in range(i+1,len(graph)):
            if graph[i][j]==1:
                temp1=find(i,check)
                temp2=find(j,check)
                if temp1==temp2:
                    print('loop exist')
                    flag=True
                    break
                else:
                    check=union(temp1,temp2,check)
        if flag:
            break
    if not flag:
        print('loop doen\'t exist')


graph=[]
graph.append([0,0,0,1,0,0,1,0])
graph.append([0,0,0,1,0,0,0,0])
graph.append([0,0,0,1,0,0,0,0])
graph.append([1,1,1,0,1,0,0,0])
graph.append([0,0,0,1,0,1,0,0])
graph.append([0,0,0,0,1,0,1,1])
graph.append([1,0,0,0,0,1,0,0])
graph.append([0,0,0,0,0,1,0,0])
unionfind(graph)
