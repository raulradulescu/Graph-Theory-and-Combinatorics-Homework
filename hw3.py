def rank_r_permutation_with_repetition(permutation, n):
    """
    Computes the rank of the r-permutation with repetition (x1, x2, ..., xr)
    of A = {1, 2, ..., n} in lexicographic order.
    """
    r = len(permutation)
    rank = 0
    for i in range(r):
        rank += (permutation[i] - 1) * (n ** (r - i - 1))
    return rank

def r_permutation_with_rank(k, n, r):
    """
    Computes the r-permutation with repetition of rank k for A = {1, 2, ..., n}
    in lexicographic order.
    """
    permutation = []
    for i in range(r):
        xi = (k // (n ** (r - i - 1))) + 1
        permutation.append(xi)
        k = k % (n ** (r - i - 1))
    return permutation

def next_r_permutation_with_repetition(permutation, n):
    """
    Computes the r-permutation with repetition immediately after the given
    permutation in lexicographic order.
    """
    r = len(permutation)
    for i in reversed(range(r)):
        if permutation[i] < n:
            permutation[i] += 1
            return permutation
        else:
            permutation[i] = 1
    return permutation  # If no next permutation, this wraps around to the first permutation

def grey_rank(B, A):
    """
    Computes the rank of subset B from set A using Grey code method.
    """
    rank = 0
    for i in range(len(B)):
        if B[i] == 1:
            rank ^= (1 << i)
    return rank

def unrank_grey(A, r):
    """
    Computes the subset of A that corresponds to the given Grey rank r.
    """
    n = len(A)
    subset = []
    for i in range(n):
        if (r >> i) & 1:
            subset.append(A[i])
    return subset

def next_grey_rank_subset(A, B):
    """
    Computes the next subset of A after subset B based on Grey code ranking.
    """
    n = len(A)
    m = grey_rank(B, A)
    next_rank = (m + 1) % (2 ** n)  # Wraps around if it reaches the end
    return unrank_grey(A, next_rank)

def display_menu():
    print("Menu:")
    print("1. Compute the rank of an r-permutation with repetition.")
    print("2. Compute the r-permutation with repetition given a rank.")
    print("3. Compute the next r-permutation with repetition in lexicographic order.")
    print("4. Compute the Grey rank of a subset.")
    print("5. Compute the next subset based on Grey code.")
    print("6. Exit.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, 3, 4, 5 or 6 to exit): ")

        if choice == '1':
            print("\nYou chose to compute the rank of an r-permutation with repetition.")
            n = int(input("Enter the size of the set A = {1, ..., n}: "))
            r = int(input("Enter the size of the permutation (r): "))
            permutation = [int(x) for x in input(f"Enter the permutation of size {r}, separated by spaces: ").split()]
            rank = rank_r_permutation_with_repetition(permutation, n)
            print(f"The rank of the permutation {permutation} is: {rank}\n")

        elif choice == '2':
            print("\nYou chose to compute the r-permutation with repetition given a rank.")
            n = int(input("Enter the size of the set A = {1, ..., n}: "))
            r = int(input("Enter the size of the permutation (r): "))
            k = int(input("Enter the rank: "))
            permutation = r_permutation_with_rank(k, n, r)
            print(f"The permutation with rank {k} is: {permutation}\n")

        elif choice == '3':
            print("\nYou chose to compute the next r-permutation with repetition.")
            n = int(input("Enter the size of the set A = {1, ..., n}: "))
            r = int(input("Enter the size of the permutation (r): "))
            permutation = [int(x) for x in input(f"Enter the current permutation of size {r}, separated by spaces: ").split()]
            next_permutation = next_r_permutation_with_repetition(permutation, n)
            print(f"The next permutation after {permutation} is: {next_permutation}\n")

        elif choice == '4':
            print("\nYou chose to compute the Grey rank of a subset.")
            A = [int(x) for x in input("Enter the set A (e.g., 1 2 3): ").split()]
            B = [int(x) for x in input(f"Enter the subset of size {len(A)}, use 1 for elements in subset, 0 otherwise: ").split()]
            rank = grey_rank(B, A)
            print(f"The Grey rank of the subset {B} is: {rank}\n")

        elif choice == '5':
            print("\nYou chose to compute the next subset based on Grey code.")
            A = [int(x) for x in input("Enter the set A (e.g., 1 2 3): ").split()]
            B = [int(x) for x in input(f"Enter the subset of size {len(A)}, use 1 for elements in subset, 0 otherwise: ").split()]
            next_subset = next_grey_rank_subset(A, B)
            print(f"The nex4t subset after {B} in Grey code order is: {next_subset}\n")

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select option 1, 2, 3, 4, 5, or 6.\n")

if __name__ == "__main__":
    main()
