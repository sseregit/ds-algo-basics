class UndirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            if v2 not in self.adj_list[v1]:
                self.adj_list[v1].append(v2)
            if v1 not in self.adj_list[v2]:
                self.adj_list[v2].append(v1)

    def display(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}: {edges}")

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=' ')

        for neighbor in self.adj_list[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')

            for neighbor in self.adj_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


graph = UndirectedGraph()
vertices = ['A', 'B', 'C', 'D', 'E']

for vertex in vertices:
    graph.add_vertex(vertex)

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')

print("Undirected Graph adjacency list:")
graph.display()

print("\nDFS traversal:")
graph.dfs('A')

print("\nBFS traversal:")
graph.bfs('A')