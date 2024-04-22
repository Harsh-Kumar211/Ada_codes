import heapq

def prims_algorithm(graph):
    mst = set() 
    visited = set()  
    start_vertex = list(graph.keys())[0]  

    priority_queue = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    heapq.heapify(priority_queue)

    while priority_queue:
        weight, u, v = heapq.heappop(priority_queue)
        if v not in visited:
            visited.add(v)
            mst.add((min(u, v), max(u, v))) 
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, v, neighbor))

    return mst

# Example usage
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

mst = prims_algorithm(graph)
print("Minimum Spanning Tree:", mst)
