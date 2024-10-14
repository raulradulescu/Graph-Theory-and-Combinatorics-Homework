def next_permutation(p):
    n = len(p)
    i = n - 2
    while i >= 0 and p[i] >= p[i + 1]:
        i -= 1

    if i == -1:
        return False  # This is the last permutation

    j = n - 1

    # Find the largest index j such that p[j] > p[i]
    while p[j] <= p[i]:
        j -= 1

    # Swap p[i] with p[j]
    p[i], p[j] = p[j], p[i]

    # Reverse the sequence from p[i + 1] to the end
    p[i + 1:] = reversed(p[i + 1:])
    return True

# Get user input for the permutation
user_input = input("Enter the permutation (space-separated numbers): ").split()
permutation = list(map(int, user_input))

if next_permutation(permutation):
    print(f"Next permutation: {permutation}")
else:
    print("This is the last permutation.")
