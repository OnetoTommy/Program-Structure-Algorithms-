class UnionFind:
    def __init__(self, n):
        # Constructor to create
        self.ranks = [1] * n
        self.parents = [i for i in range(n)]
 
    # Finds set of given item u
    def find(self, u):
        # Finds the representative of the set
        # that x is an element of
        if (self.parents[u] != u):
            # path compression technique
            self.parents[u] = self.find(self.parents[u])
 
        return self.parents[u]
 
 
    # Do union of two sets represented by u and v.
    def union(self, u, v):
        # Find current sets of u and v
        xset = self.find(u)
        yset = self.find(v)
 
        # If they are already in same set
        if xset == yset:
            return
 
        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.ranks[xset] < self.ranks[yset]:
            self.parents[xset] = yset
 
        elif self.ranks[xset] > self.ranks[yset]:
            self.parents[yset] = xset
 
        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parents[yset] = xset
            self.ranks[xset] = self.ranks[xset] + 1
 
# Driver code
obj = UnionFind(5)
obj.union(0, 2)
obj.union(4, 2)
obj.union(3, 1)
obj.union(2, 3)
if obj.find(4) == obj.find(0):
    print('Yes')
else:
    print('No')
if obj.find(1) == obj.find(0):
    print('Yes')
else:
    print('No')