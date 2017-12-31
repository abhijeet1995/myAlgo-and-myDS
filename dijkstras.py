class Graph:
    @classmethod
    def minDis(cls, path, visited):
        dis = float('inf')
        for i in range(0, len(path)):
            if not visited[i] and path[i] <= dis:
                dis = path[i]
                disindex = i
        return disindex

    @classmethod
    def print_path(cls, path):
        for i in range(0, len(path)):
            print(path[i], end='   ')

    @classmethod
    def dijkstra(cls, graph, src):
        path = [float('inf')]*len(graph)
        visited = [False]*len(graph)
        path[src] = 0
        for count in range(0, len(graph)-1):
            u=cls.minDis(path, visited)
            visited[u] = True
            for v in range(0, len(graph)):
                if not visited[v] and graph[u][v] != 0 and path[u]+graph[u][v] < path[v]:
                    path[v] = graph[u][v]+path[u]
        cls.print_path(path)

graph=[]
graph.append([0, 4, 0, 0, 0, 0, 0, 8, 0])
graph.append([4, 0, 8, 0, 0, 0, 0, 11, 0])
graph.append([0, 8, 0, 7, 0, 4, 0, 0, 2])
graph.append([0, 0, 7, 0, 9, 14, 0, 0, 0])
graph.append([0, 0, 0, 9, 0, 10, 0, 0, 0])
graph.append([0, 0, 4, 14, 10, 0, 2, 0, 0])
graph.append([0, 0, 0, 0, 0, 2, 0, 1, 6])
graph.append([8, 11, 0, 0, 0, 0, 1, 0, 7])
graph.append([0, 0, 2, 0, 0, 0, 6, 7, 0])
Graph.dijkstra(graph, 0)
