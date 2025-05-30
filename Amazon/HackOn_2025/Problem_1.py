# Problem:
# You are given a string which represents a rope, where each character in the string corresponds to a 1 meter segment of rope. 
# The length of rope is 'N'. Each segment of the rope can either have a knot ('2') or no knot ('1').
# You are also given an integer 'K'. You have to fold the rope K times. 
# In each fold, divide the rope into two equal parts and reverse the second half, then overlay the two parts by summing corresponding segments.
# After folding K times, determine the strength of each segment in the resulting rope.
# A knot ('2') contributes strength of 2 and a plain segment ('1') contributes 1.

# Input Format:
# First line: Two space-separated integers 'N' and 'K' (length of the rope and number of folds)
# Second line: A string of length N containing only '1's and '2's

# Output Format:
# Output an array of space-separated integers representing the strength of each segment in the final rope

# Constraints:
# 1 <= N <= 10^6
# 0 <= K <= log2(N)

# Sample Testcase 1:
# Input:
# 8 2
# 12212121
# Output:
# 5 7

# Sample Testcase 2:
# Input:
# 4 1
# 1221
# Output:
# 2 4
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#SOLUTION- 

def fold_rope(N, K, rope):
    # Convert each character in the rope string to an integer (1 or 2) to represent initial strength
    strength = [int(c) for c in rope]
    
    # Perform folding K times
    for _ in range(K):
        # Find the halfway point for folding
        half = len(strength) // 2
        
        # Fold the rope: overlay first half with reversed second half
        # strength[i] + strength[-1 - i] means adding i-th element from front and i-th from back
        folded = [strength[i] + strength[-1 - i] for i in range(half)]
        
        # Update strength list to the newly folded rope
        strength = folded
    
    # Print the final strength values as space-separated integers
    print(*strength)

# Read two integers from input: N (length of rope) and K (number of folds)
N, K = map(int, input().split())

# Read the rope string and remove any trailing newline or spaces
rope = input().strip()

# Call the function to process the folding and print the result
fold_rope(N, K, rope)
