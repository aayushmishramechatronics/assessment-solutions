#SOLUTION 

# DSU (Disjoint Set Union) class to manage connected components
class DSU:
    def __init__(self, n, weights):
        # Each town initially points to itself as its own parent
        self.parent = list(range(n))
        # Each town starts as its own component, so total_weight is initialized with the node's resource
        self.total_weight = weights[:]

    def find(self, x):
        # Path compression: find the root parent of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Recursively find and flatten the path
        return self.parent[x]

    def get_weight(self, x):
        # Get total resource weight of the component x belongs to
        return self.total_weight[self.find(x)]

    def union(self, x, y):
        # Find roots of both components
        xr = self.find(x)
        yr = self.find(y)
        # If already in the same component, no union needed
        if xr == yr:
            return False
        # Merge the smaller component into the larger one to keep tree depth low
        if self.total_weight[xr] < self.total_weight[yr]:
            xr, yr = yr, xr
        # Set parent of smaller to larger
        self.parent[yr] = xr
        # Add weights of the two components
        self.total_weight[xr] += self.total_weight[yr]
        return True

# Read number of towns (nodes) and bridges (edges)
n, m = map(int, input().split())

# Read the resource weights of each town (0-indexed internally)
weights = list(map(int, input().split()))

# Read all bridges: each bridge connects Ai and Bi with strength requirement Yi
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Sort bridges by decreasing strength requirement (so stronger bridges are handled first)
edges.sort(key=lambda x: -x[2])

# Initialize DSU structure with town weights
dsu = DSU(n, weights)

# Count of bridges that must be removed
removed = 0

# Process each bridge
for u, v, w in edges:
    # Convert to 0-based indexing
    u -= 1
    v -= 1
    # Find the root of both towns
    ru = dsu.find(u)
    rv = dsu.find(v)

    if ru == rv:
        # The towns are already in the same component
        # Check if this component has enough resource to support the bridge
        if dsu.get_weight(u) < w:
            removed += 1  # Not enough support, remove the bridge
    else:
        # The towns are in different components
        # Check if combining them creates a strong enough component to support this bridge
        if dsu.get_weight(u) + dsu.get_weight(v) >= w:
            dsu.union(u, v)  # Safe to merge
        else:
            removed += 1  # Not enough combined support, must remove the bridge

# Print the total number of bridges that had to be removed
print(removed)
