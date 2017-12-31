class Graph:
    @classmethod
    def find(cls,i,check):
        if check[i]==-1:
            return i
        else:
            while check[check[i]]!=-1:
                i=check[i]
            return check[i]

    @classmethod
    def union(cls,i,j,check):
        check[i]=j
        return check

    @classmethod
    def kruskals(cls,graph):
        edge=[]
        for i in range(0,len(graph)):
            for j in range(i+1,len(graph)):
                if graph[i][j]!=0:
                    edge.append([graph[i][j],i,j])
        edge.sort()
        s=0
        check=[-1]*len(graph)
        for element in edge:
            temp1=cls.find(element[1],check)
            temp2=cls.find(element[2],check)
            if temp1!=temp2:
                s=s+element[0]
                check=cls.union(temp1,temp2,check)
        print(s)
graph=[]
graph.append([0,4,0,0,0,0,0,8,0])
graph.append([4,0,8,0,0,0,0,11,0])
graph.append([0,8,0,7,0,4,0,0,2])
graph.append([0,0,7,0,9,14,0,0,0])
graph.append([0,0,0,9,0,10,0,0,0])
graph.append([0,0,4,14,10,0,2,0,0])
graph.append([0,0,0,0,0,2,0,1,6])
graph.append([8,11,0,0,0,0,1,0,7])
graph.append([0,0,2,0,0,0,6,7,0])
Graph.kruskals(graph)
