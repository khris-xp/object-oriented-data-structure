def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_distance_node = None
        for node in graph:
            if node not in visited and (min_distance_node is None or distance[node] < distance[min_distance_node]):
                min_distance_node = node

        for neighbor, weight in graph[min_distance_node].items():
            if distance[min_distance_node] + weight < distance[neighbor]:
                distance[neighbor] = distance[min_distance_node] + weight

        visited.add(min_distance_node)

    return distance

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

for node, distance in shortest_distances.items():
    print(f"Shortest distance from {start_node} to {node} is {distance}")