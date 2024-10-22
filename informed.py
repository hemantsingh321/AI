from queue import PriorityQueue

v = 14
graph = [[] for _ in range(v)]

def best_first_search(source, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, source))
    visited[source] = True
    
    while not pq.empty():
        current_node = pq.get()[1]
        print(current_node, end=" ")

        if current_node == target:
            break
        
        for neighbor, cost in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                pq.put((cost, neighbor))
    print()

def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

add_edge(0, 1, 3)
add_edge(0, 2, 6)
add_edge(0, 3, 5)
add_edge(1, 4, 9)
add_edge(1, 5, 8)
add_edge(2, 6, 12)
add_edge(2, 7, 14)
add_edge(3, 8, 7)
add_edge(8, 9, 5)
add_edge(8, 10, 6)
add_edge(9, 11, 1)
add_edge(9, 12, 10)
add_edge(9, 13, 2)

source = 0
target = 9

best_first_search(source, target, v)
