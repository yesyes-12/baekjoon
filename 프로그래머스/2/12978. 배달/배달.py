import heapq
def solution(N, road, K):
    answer = 0
    
    graph = {}
    for start, end, weight in road:
        if start not in graph: graph[start] = []
        graph[start].append((end, weight))
        
        if end not in graph: graph[end] = []
        graph[end].append((start,weight))
        
    #print(graph)
    
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        #print(distances)
        
        queue = [(0,1)]
        
        while queue:
            curr_dis, curr_node = heapq.heappop(queue)
            if distances[curr_node] < curr_dis:
                continue
                
            for next_node, weight in graph[curr_node]:
                dis = curr_dis + weight
                
                if dis < distances[next_node]:
                    distances[next_node] = dis
                    heapq.heappush(queue,(dis,next_node))

        return sum(1 for weight in distances.values() if weight <= K)
    
    answer = dijkstra(graph,1)
    return answer

