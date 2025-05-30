#Problem Statement - Course Cluster Compression

#At SkillBrew, students enroll in a wide range of micro-courses. Each course has a scheduled start and end time. 
#However, due to limited instructor akailability, multiple courses that overlap or are adjacent can be taught together in a single teaching block.
#You are given courses, where each course is represented by a pair of integers [start, end]. 
#Two courses can be merged into one block if the start time of one is less than or equal to the end time of another.
#Your task is to determine the minimum number of non-overlapping teaching blocks required to cover all the courses at SkillBrew.

#Input Format:
#The first line contains an integer n the number of courses.
#The next in lines each contain two integers start and end the start and end time of a course.

#Output Format:
#Print a single integer - the number of compressed (merged) time blocks required to cover all courses.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#SOLUTION 

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
