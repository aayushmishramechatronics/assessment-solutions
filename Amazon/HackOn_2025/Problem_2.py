#Problem -
#In the mystical realm of Graphoria, the kingdom is a network of ancient towns and bridges. 
#Each town, uniquely numbered from 1 to N, is endowed with its own reservoir of resources, represented by its weight. 
#Meanwhile, the bridges-numbered from 1 to M-span the distances between these towns, each with a strength requirement indicated by its weight.
#The wise elders of Graphoria decree that for every bridge that remains standing,
#the combined resources of all the towns in the connected region (the connected component) must be at least as great as the strength requirement of that bridge. 
#In other words, the towns must collectively be powerful enough to support the bridge.
#Your quest is to help the kingdom by removing the fewest number of bridges necessary so that every remaining bridge is adequately supported by the resources of its connected towns. 
#Can you determine the minimum number of bridges that must be dismantled to ensure that the entire network of towns and bridges remains strong and secure under this decree?

#Input Format - 
#The first line of input contains two space-separated integers N denotes the number of vertices and M denotes the number of edges.
#The second line of input contains N space separated integers X1,X2,..., XN representing the weights of the vertices.
#Each of the next M lines contains three space separated integers Ai, Bi, Yi representing an edge between vertices Ai and Bi with weight Yi.

#Output Format
#Print a single integer representing the minimum number of edges that need to be removed to satisfy the condition.

#Constraints -
#1≤ N ≤ 10^3
#N-1≤ M ≤  (N*(N-1))/2
#1 ≤ Xi ≤ 10^9
#1 ≤ Ai < Bi ≤ N
#1 ≤ Yi ≤ 10^9

#Sample Testcase 1

#Testcase Input
#6 10
#4 4 11 17
#3 5 19
#2 5 20
#4 5 8
#1 6 16
#2 3 9
#3 6 16
#3 4 1
#2 6 20
#2 4 19
#1 2 9

#Testcase Output
#4

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

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
