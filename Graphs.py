class Graphs:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_List = dict()  # corrected spelling

    def __repr__(self):
        graph_string = ""
        for node, neighbours in self.adj_List.items():
            graph_string += f"{node} -> {neighbours}\n"
        return graph_string

    def add_node(self, node):
        if node not in self.adj_List:
            self.adj_List[node] = set()
        else:
            raise ValueError("Node already exists")

    def add_edge(self, from_node, to_node, weight=None):  # added weight
        if from_node not in self.adj_List:
            self.add_node(from_node)
        if to_node not in self.adj_List:
            self.add_node(to_node)

        if weight is None:
            self.adj_List[from_node].add(to_node)
            if not self.directed:
                self.adj_List[to_node].add(from_node)
        else:
            self.adj_List[from_node].add((to_node, weight))
            if not self.directed:
                self.adj_List[to_node].add((from_node, weight))

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.obtain_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        queue.append(neighbour)
        return order

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbours = self.obtain_neighbours(node)
                for neighbour in neighbours:
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]
                    if neighbour not in visited:
                        stack.append(neighbour)
        return order

    def obtain_neighbours(self, node):
        return self.adj_List.get(node, set())


if __name__ == '__main__':
    graph_obj = Graphs(directed=True)

    graph_obj.add_edge("A", "B", 2)
    graph_obj.add_edge("A", "J", 6)
    graph_obj.add_edge("A", "C", 3)
    graph_obj.add_edge("B", "D", 4)
    graph_obj.add_edge("D", "C", 7)

    print("GRAPH STRUCTURE:\n", graph_obj)
    print("BREADTH FIRST SEARCH:\n", graph_obj.bfs("A"))
    print("DEPTH FIRST SEARCH:\n", graph_obj.dfs("A"))
