# Problem Statement - Persistent Segment Tree with Range Sum Queries

You are given an array of in integers and need to support two types of queries using a persistent segment tree:
1. Point Update: Update a specific index to a new value in a given version, resulting in a new version of the segment tree.
2. Range Sum Query: Query the sum of elements in a subarray range [l. r) on a specified array version.
Each update creates a new version of the array. Your task is to efficiently handling these operations while preserving access to all previous versions.

# Input Format:
The first line contains two integers n and q-the size of the array and the number of queries.
The second line contains in integers a1, a2,..., an the initial array values.
The next a lines contain queries:
-1 vix-Update index i (1-based) to value x on version v. creating a new version.
-2 vlr-Query the sum in range [l, r] (1-based inclusive) on version v.

# Output Format:
For each query of type 2, output the result on a new line.

# Constraints:

a) 1 ≤ n ≤ 10 ^ 5
b) 1 ≤ q ≤ 10 ^ 5
c) 1 ≤ ai,x ≤ 10 ^ 9
d) 1 ≤ v ≤ number of versions created
e) 1 ≤ l ≤ r ≤ n

# Example: 0
# Input:

5 5
/
1 2 3 4 5
/
2 1 2 4
/
1 1 3 10
/
2 2 1 5
/
2 1 3 3
/
2 2 3 3

# Output:

9
/
22
/
3
/
10

# Explanation for the Example: 0

Initial version 1: [1, 2, 3, 4, 5]
a) Query 2 1 2 4 Sum of [2, 3, 4] = 2 + 3 + 4 = 9
b) Update 1 1 3 10 -> Set index 3 to 10 in version 1, creating version 2: [1, 2, 10, 4, 5]
c) Query 2 2 1 5 -> Sum of [1, 2, 10, 4, 5] = 22
d) Query 2 1 3 3 -> Sum at index 3 in version 1 = 3
e) Query 2 2 3 3 -> Sum at index 3 in version 2 = 10

# Example: 1
# Input:

3 3
/
1 1 1
/
1 1 2 5
/
2 2 1 3
/
2 1 1 3

# Output:

7
/
3

# Explanation for the Example: 1

Initial version 1: [1, 1, 1)
a) Update 1 1 2 5 -> Set Index 2 to 5 in version 1, creating version 2: [1, 5, 1]
b) Query 2 2 1 3 -> Sum of [1, 5, 1] = 7
c) Query 2 1 1 3 -> Sum of [1, 1, 1]= 3
