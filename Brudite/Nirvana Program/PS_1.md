# Problem Statement - Course Cluster Compression

At SkillBrew, students enroll in a wide range of micro-courses. Each course has a scheduled start and end time. 
However, due to limited instructor akailability, multiple courses that overlap or are adjacent can be taught together in a single teaching block.
You are given courses, where each course is represented by a pair of integers [start, end]. 
Two courses can be merged into one block if the start time of one is less than or equal to the end time of another.
Your task is to determine the minimum number of non-overlapping teaching blocks required to cover all the courses at SkillBrew.

# Input Format:
The first line contains an integer n the number of courses.
The next in lines each contain two integers start and end the start and end time of a course.

# Output Format:
Print a single integer - the number of compressed (merged) time blocks required to cover all courses.

# Constraints:
a) 1 ≤ n ≤ 10^5
b) 0 ≤ start < end ≤ 10^9

# Example: 0
# Input:

'5
1 5
3 7
8 10
9 12
13 15'

# Output:
'3'

# Explanation for the Example: 0

# Merge [1, 5] and [3, 7] → [1, 7]
# Merge [8, 10] and [9, 12] → [8, 12]
# [3, 15] stays as is
# Hence, total blocks = 3

# Example: 1
# Input:
'4
1 2'

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
