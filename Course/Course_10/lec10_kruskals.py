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
  
    # Find set of an element i (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] != i: 
            # Reassignment of node's parent to root node
            parent[i] = self.find(parent, parent[i]) 
        return parent[i]
    
  
    # Union of two sets of x and y (by rank) 
    def union(self, parent, rank, x, y): 
        # Attach smaller rank tree under root of high rank tree
        if rank[x] < rank[y]: 
            parent[x] = y 
        elif rank[x] > rank[y]: 
            parent[y] = x 
  
        # If ranks are same, then make one as root and increment its rank by one 
        else: 
            parent[y] = x 
            rank[x] += 1
  
    def run_kruskal(self): 
        result = [] 
        i = 0
        e = 0
  
        # Sort all the edges in non-decreasing order of their weighta 
        self.graph = sorted(self.graph, 
                            key=lambda item: item[2]) 
  
        parent = [] 
        rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
  
        while e < self.V - 1: 
            # Pick the smallest edge and increment the index for next iteration 
            u, v, w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
  
            # If including this edge doesn't 
            # cause cycle, then include it in result 
            # and increment the index of result 
            # for next edge 
            if x != y: 
                e = e + 1
                result.append([u, v, w]) 
                self.union(parent, rank, x, y) 
            # Else discard the edge 
  
        minimumCost = 0
        print("Edges in the constructed MST using Kruskal's") 
        for u, v, weight in result: 
            minimumCost += weight 
            #print("%s (%d) -- %s (%d) == %d" % (self.id_to_name[u], u, self.id_to_name[v], v, weight)) 
            print("%s -- %s  == %d" % (self.id_to_name[u], self.id_to_name[v], weight)) 
        print("Minimum Spanning Tree Cost: ", minimumCost) 
  
  
# Driver code 
if __name__ == '__main__': 
    ex = 4
    if ex == 1:
        g = Graph(9)
        g.add_edge("a", "b", 10) 
        g.add_edge("a", "c", 12) 
        g.add_edge("b", "c", 9) 
        g.add_edge("b", "d", 8) 
        g.add_edge("c", "e", 3)
        g.add_edge("c", "f", 1)
        g.add_edge("d", "e", 7)
        g.add_edge("d", "g", 8)
        g.add_edge("d", "h", 5)
        g.add_edge("e", "f", 3)
        g.add_edge("f", "h", 6)
        g.add_edge("g", "h", 9)
        g.add_edge("g", "i", 2)
        g.add_edge("h", "i", 11)

    elif ex == 2:
        g = Graph(6)
        g.add_edge("A", "B", 5) 
        g.add_edge("A", "C", 6) 
        g.add_edge("A", "D", 4) 
        g.add_edge("B", "C", 1) 
        g.add_edge("B", "D", 2)
        g.add_edge("C", "D", 2)
        g.add_edge("C", "E", 5)
        g.add_edge("C", "F", 3)
        g.add_edge("D", "F", 4)
        g.add_edge("E", "F", 4)
        
    elif ex == 3:
        g = Graph(4)
        g.add_edge(0, 1, 10) 
        g.add_edge(0, 2, 6) 
        g.add_edge(0, 3, 5) 
        g.add_edge(1, 3, 15) 
        g.add_edge(2, 3, 4)

    elif ex == 4:
        g = Graph(5)
        g.add_edge("s", "u", 6) 
        g.add_edge("s", "t", 3) 
        g.add_edge("s", "v", 2) 
        g.add_edge("t", "u", 5) 
        g.add_edge("t", "v", 4)
        g.add_edge("t", "w", 5)
        g.add_edge("u", "w", 1)
        g.add_edge("u", "v", 4)
        g.add_edge("v", "w", 6)
  
    # Function call 
    g.run_kruskal() 