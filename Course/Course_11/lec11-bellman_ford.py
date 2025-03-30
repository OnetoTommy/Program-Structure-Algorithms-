class Graph:

    def __init__(self, numV):
        self.V = numV
        self.graph = []
        self.id_to_name = {}
        self.name_to_id = {}
        self.currId = 0

    def add_edge(self, u, v, w):
        uId = vId = -1
        if u not in self.name_to_id:
            uId = self.currId
            self.id_to_name[self.currId] = u
            self.name_to_id[u] = uId
            self.currId += 1
        else:
            uId = self.name_to_id[u]

        if v not in self.name_to_id:
            vId = self.currId
            self.id_to_name[self.currId] = v
            self.name_to_id[v] = vId
            self.currId += 1
        else:
            vId = self.name_to_id[v]
        
        self.graph.append([uId, vId, w])

    # print the solution
    def printSol(self, dist):
        print("Vertex Distance from Source")
        for uId in range(self.V):
            print("{0}\t\t{1}".format(self.id_to_name[uId], dist[uId]))

    def run_BellmanFord(self, src):
        if isinstance(src, str):
            src = self.name_to_id[src]
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        self.printSol(dist)


# Driver's code
if __name__ == '__main__':

    ex = 2

    if ex == 1:
        g = Graph(5)
        g.add_edge(0, 1, -1)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 2)
        g.add_edge(1, 4, 2)
        g.add_edge(3, 2, 5)
        g.add_edge(3, 1, 1)
    elif ex == 2:
        g = Graph(4)
        g.add_edge("s", "1", 3)
        g.add_edge("s", "3", 2)
        g.add_edge("s", "4", 2)
        g.add_edge("1", "3", -2)
        g.add_edge("3", "4", -1)

    ## run
    g.run_BellmanFord(0)

