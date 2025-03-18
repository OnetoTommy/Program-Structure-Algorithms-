import heapq

class Graph: 
    def __init__(self, numV): 
        self.V = numV
        self.adj = [[] for _ in range(numV)]
        self.id_to_name = {}
        self.name_to_id = {}
        self.currId = 0
        self.prev = {}
  
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

        self.adj[uId].append((vId, w))
        self.adj[vId].append((uId, w))

    def run_prims(self, src=0):       
        # Initialize all distances as infinite (INF)
        cost = [float('inf')] * self.V
        cost[src] = 0
        pq = [(cost[src], src)]
 
        # Looping until the pq becomes empty
        result = []
        minimumCost = 0
        while pq:
            # Extract the vertex with min weight from the pq
            current_cost, u = heapq.heappop(pq)
            if u in result:
                #print("%d is explored"%(u))
                continue

            result.append(u)
            #print("Deletemin: %d"%(u))
            minimumCost += current_cost
            
            # Iterate over all adjacent vertices of a vertex
            for v, weight in self.adj[u]:
                if v in result:
                    continue
                # If there is a smaller cost for v
                if cost[v] > weight:
                    # Update the distance of v
                    cost[v] = weight
                    self.prev[v] = u
                    #print("%d %d %d"%(u, v, cost[v]))
                    heapq.heappush(pq, (cost[v], v))

 

        #print(result)
        print("Edges in the constructed MST using Prim's")
        for u in range(1, self.V):
            for v_iter, weight in self.adj[u]:
                if v_iter == self.prev[u]:
                    print("%s -- %s  == %d" % (self.id_to_name[u], self.id_to_name[self.prev[u]], weight)) 
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
    g.run_prims() 