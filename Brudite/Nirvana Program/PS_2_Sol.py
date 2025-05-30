# Read two integers from input: n = number of elements in array, q = number of queries
n, q = map(int, input().split())

# Read the initial array of n integers
arr = list(map(int, input().split()))

# Initialize a list to store different versions of the array.
# Version 0 is the initial array.
versions = [arr[:]]  # use arr[:] to create a shallow copy

# Process each of the q queries
for _ in range(q):
    # Read the current query into a list of integers
    temp = list(map(int, input().split()))

    # If the query is of type 1 (update operation)
    if temp[0] == 1:
        v, i, x = temp[1]-1, temp[2]-1, temp[3]
        # v = version number to base this update on (0-based index)
        # i = index in the array to update (0-based index)
        # x = new value to be placed at index i

        # Make a copy of version 'v' to create a new version (copy-on-write)
        new_version = versions[v][:]
        
        # Apply the update to index i
        new_version[i] = x
        
        # Store the new version as a new snapshot in versions
        versions.append(new_version)

    else:
        # If the query is of type 2 (range sum query)
        v, l, r = temp[1]-1, temp[2]-1, temp[3]-1
        # v = version number to query from (0-based index)
        # l, r = range [l, r] inclusive (0-based indices)

        # Calculate and print the sum of the subarray from l to r in version v
        print(sum(versions[v][l:r+1]))
