import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import heapq

class GraphVisualizer:
    def __init__(self):
        self.G = nx.Graph()
        self.pos = None
    
    def create_graph(self, edges):
        self.G.clear()
        for u, v, cost in edges:
            self.G.add_edge(u, v, weight=cost)
        self.pos = nx.spring_layout(self.G, seed=42)
    
    def plot_initial_graph(self):
        plt.figure(figsize=(6, 4), num="Initial Graph")
        
        nx.draw_networkx_nodes(self.G, self.pos, node_size=500, 
                              node_color='lightblue')
        nx.draw_networkx_labels(self.G, self.pos, font_size=12, 
                               font_weight='bold')
        nx.draw_networkx_edges(self.G, self.pos, edge_color='gray', 
                              width=2)
        
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.pos, 
                                    edge_labels=edge_labels)
        
        plt.title("Initial Graph Structure")
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def plot_algorithm(self, path, title):
        plt.figure(figsize=(6, 4))
        
        nx.draw_networkx_nodes(self.G, self.pos, node_size=500, 
                              node_color='lightblue')
        nx.draw_networkx_labels(self.G, self.pos, font_size=12, 
                               font_weight='bold')
        nx.draw_networkx_edges(self.G, self.pos, edge_color='gray', 
                              width=1)
        
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.pos, 
                                    edge_labels=edge_labels)
        
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(self.G, self.pos, edgelist=path_edges, 
                              edge_color='red', width=3)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=path, 
                              node_size=600, node_color='yellow')
        
        plt.title(title)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

class GraphAlgorithms:
    def __init__(self, edges):
        self.graph = {}
        for u, v, cost in edges:
            self.add_edge(u, v, cost)
        self.visualizer = GraphVisualizer()
        self.visualizer.create_graph(edges)
    
    def add_edge(self, u, v, cost=1):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))
    
    def bfs(self, start, target):
        visited = set()
        queue = deque([[start]])
        visited.add(start)
        
        while queue:
            path = queue.popleft()
            node = path[-1]
            
            if node == target:
                self.visualizer.plot_algorithm(path, 
                    f"BFS Path: {' → '.join(path)}")
                return path
            
            for neighbor, _ in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        
        return None
    
    def dfs(self, start, target):
        visited = set()
        stack = [[start]]
        
        while stack:
            path = stack.pop()
            node = path[-1]
            
            if node in visited:
                continue
            
            visited.add(node)
            
            if node == target:
                self.visualizer.plot_algorithm(path, 
                    f"DFS Path: {' → '.join(path)}")
                return path
            
            neighbors = sorted(self.graph.get(node, []), reverse=True)
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
        
        return None
    
    def dijkstra(self, start, target):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start, [start])]
        visited = set()
        
        while pq:
            current_dist, current, path = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            if current == target:
                self.visualizer.plot_algorithm(path, 
                    f"Dijkstra Path: {' → '.join(path)} (Cost: {current_dist})")
                return path, current_dist
            
            for neighbor, cost in self.graph.get(current, []):
                if neighbor not in visited:
                    new_dist = current_dist + cost
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        new_path = path + [neighbor]
                        heapq.heappush(pq, (new_dist, neighbor, new_path))
        
        return None, float('inf')

edges = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'D', 5), ('C', 'D', 8),
    ('C', 'E', 10), ('D', 'F', 6),
    ('E', 'F', 3), ('D', 'E', 2)
]

algo = GraphAlgorithms(edges)

algo.visualizer.plot_initial_graph()

bfs_path = algo.bfs('A', 'F')
dfs_path = algo.dfs('A', 'F')
dijkstra_path, dijkstra_cost = algo.dijkstra('A', 'F')

print(f"\nBFS Path (Shortest Steps):")
print(f"  Path: {' → '.join(bfs_path)}")
print(f"  Number of steps: {len(bfs_path)-1}")

print(f"\nDFS Path (Depth First):")
print(f"  Path: {' → '.join(dfs_path)}")
print(f"  Number of steps: {len(dfs_path)-1}")

print(f"\nDijkstra Path (Lowest Cost):")
print(f"  Path: {' → '.join(dijkstra_path)}")
print(f"  Total cost: {dijkstra_cost}")

path_costs = {
    'BFS': sum([cost for u,v,cost in edges 
                if (u,v) in zip(bfs_path, bfs_path[1:]) or 
                   (v,u) in zip(bfs_path, bfs_path[1:])]),
    'DFS': sum([cost for u,v,cost in edges 
                if (u,v) in zip(dfs_path, dfs_path[1:]) or 
                   (v,u) in zip(dfs_path, dfs_path[1:])]),
    'Dijkstra': dijkstra_cost
}

print(f"BFS Path Cost: {path_costs['BFS']}")
print(f"DFS Path Cost: {path_costs['DFS']}")
print(f"Dijkstra Path Cost: {path_costs['Dijkstra']}")