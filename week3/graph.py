class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph:
            self.graph[node_a] = [node_b]
        else:
            self.graph[node_a].append(node_b)

        if node_b not in self.graph:
            self.graph[node_b] = []

    def get_neighbors_for(self, node):
        return(self.graph[node])

    def path_between(self, node_a, node_b):
        if node_b not in self.graph or node_b not in self.graph:
            return False

        elif node_a in self.get_neighbors_for(node_a):
            return True

        elif node_b in self.get_neighbors_for(node_b):
            return True
