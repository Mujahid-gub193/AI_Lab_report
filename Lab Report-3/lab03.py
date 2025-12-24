def is_safe(v, graph, colors, c):
    for neighbor in graph[v]:
        if colors[neighbor] == c:
            return False
    return True
def graph_coloring_util(graph, k, colors, v, n):
    if v == n:
        return True
    for c in range(1, k + 1):
        if is_safe(v, graph, colors, c):
            colors[v] = c
            if graph_coloring_util(graph, k, colors, v + 1, n):
                return True
            colors[v] = 0  # Backtrack
    return False
def graph_coloring(n, graph, k):
    colors = [0] * n
    if graph_coloring_util(graph, k, colors, 0, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", colors)
    else:
        print(f"Coloring Not Possible with {k} Colors")
def read_input(filename):
    with open(filename, 'r') as file:
        n, m, k = map(int, file.readline().split())
        graph = {i: [] for i in range(n)}
        for _ in range(m):
            u, v = map(int, file.readline().split())
            graph[u].append(v)
            graph[v].append(u)
    return n, graph, k
if __name__ == "__main__":
    filename = "input.txt"  # Change file name if needed
    n, graph, k = read_input(filename)
    graph_coloring(n, graph, k)
