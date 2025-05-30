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
