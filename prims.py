class Prims:
    @classmethod
    def minDis(cls,path,visited):
        dis=float('inf')
        for i in range(0,len(path)):
            if not visited[i] and path[i]<=dis:
                dis=path[i]
                disindex=i
        return disindex

    @classmethod
    def prims(cls,graph):
        path=[float('inf')]*len(graph)
        visited=[False]*len(graph)
        path[0]=0
        s=0
        for count in range(0,len(graph)):
            u=cls.minDis(path,visited)
            visited[u]=True
            s+=path[u]
            for v in range(0,len(graph)):
                if not visited[v] and graph[u][v]!=0 and graph[u][v]<path[v]:
                    path[v]=graph[u][v]
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
Prims.prims(graph)
