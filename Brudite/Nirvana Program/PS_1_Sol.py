# Read the number of time intervals
n = int(input())

# Initialize an empty list to store the intervals
times = []

# Read each interval and store it as a tuple (start, end)
for _ in range(n):
    a, b = map(int, input().split())
    times.append((a, b))

# Sort the intervals based on the start time (default sort by first element of tuple)
times.sort()

# Initialize count of merged intervals (at least one interval exists)
count = 1

# Initialize the first interval as the starting reference
start, end = times[0]

# Loop through the remaining intervals
for i in range(1, n):
    s, e = times[i]  # current interval's start and end

    if s <= end:
        # If intervals overlap (current start is before previous end),
        # merge them by extending the end if needed
        end = max(end, e)
    else:
        # If no overlap, we have a new separate interval
        count += 1
        start, end = s, e  # update to the new interval

# Print the number of merged non-overlapping intervals
print(count)
