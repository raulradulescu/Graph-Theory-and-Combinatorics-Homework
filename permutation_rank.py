from math import factorial

def rank_of_permutation(p):
    n = len(p)
    if n == 1:
        return 0

    q = [0] * (n - 1)

    # Adjust p[1..n-1] to become a permutation of {1, ..., n-1}
    for i in range(1, n):
        if p[i] < p[0]:
            q[i - 1] = p[i]
        else:
            q[i - 1] = p[i] - 1

    # Recursive rank calculation
    return rank_of_permutation(q) + (p[0] - 1) * factorial(n - 1)

# Get user input for the permutation
user_input = input("Enter the permutation (space-separated numbers): ").split()
permutation = list(map(int, user_input))

rank = rank_of_permutation(permutation)
print(f"Rank of the permutation: {rank}")
