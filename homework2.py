import math

# 1st program
def is_permutation(sequence):
    n = len(sequence)
    expected_set = set(range(1, n + 1))
    if set(sequence) == expected_set:
        return "a permutation"
    else:
        return "not a permutation"
# 2nd program in the choice
# 3rd program
def find_rank(permutation):
    n = len(permutation)
    rank = 1
    elements = list(range(1, n + 1))

    for i in range(n):
        smaller_count = elements.index(permutation[i])
        rank += smaller_count * math.factorial(n - i - 1)
        elements.pop(smaller_count)

    return rank
# 4th program
def inverse_permutation(permutation):
    n = len(permutation)
    inverse = [0] * n

    for i in range(n):
        inverse[permutation[i] - 1] = i + 1

    return inverse
# 5th program
def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return False  # No next permutation
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True
# 6th program
def previous_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = n - 1
    while arr[j] >= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True

def show_menu():
    print('\n')
    print("Choose a program to run:")
    print("1. Check if a sequence is a permutation")
    print("2. Find the permutation with a given rank")
    print("3. Find the rank of a permutation")
    print("4. Compute the inverse of a permutation")
    print("5. Find the next permutation in lexicographic order")
    print("6. Find the previous permutation in lexicographic order")


def main():
    while True:
        show_menu()
        choice = input("Enter the number of the program you want to run (or 'exit' to quit):")

        if choice == 'exit':
            break

        try:
            choice = int(choice)
            if choice == 1:
                print("\nOption 1: Check if a sequence is a permutation.")
                sequence = list(map(int, input("Enter the sequence (space-separated): ").split())) # Get the permutation from the user
                result = is_permutation(sequence)
                print(f"The sequence is {result}.")

            elif choice == 2:
                print("\nOption 2: Find the permutation with a given rank.")
                n = int (input("Enter the number of elements in the permutation: "))
                r = int (input("Enter the rank of the permutation: "))
                if r < 0 or r > math.factorial(n)-1:
                    print ("Invalid rank")
                else:
                #for r in range(math.factorial(n)):     To display all permutations
                    perm = []
                    for i in range(1,n+1):
                        perm.append(i)
                    fact = math.factorial(n-1)
                    for i in range(n-1):
                        index = r // fact
                        print (perm[index], end = " ")
                        perm.pop(index)
                        r = r % fact
                        fact = fact // (n-i-1)
                    print (perm[0])

            elif choice == 3:
                print("\nOption 3: Find the rank of a permutation.")
                permutation = list(map(int, input("Enter the permutation (space-separated): ").split()))
                rank = find_rank(permutation)
                print(f"Rank of the permutation: {rank}")


            elif choice == 4:
                print("\nOption 4: Compute the inverse of a permutation.")
                permutation = list(map(int, input("Enter the permutation (space-separated): ").split()))
                inverse = inverse_permutation(permutation)
                print(f"Inverse of the permutation: {inverse}")


            elif choice == 5:
                print("\nOption 5: Find the next permutation in lexicographic order.")
                permutation = list(map(int, input("Enter the permutation (space-separated): ").split()))
                if next_permutation(permutation):
                    print(f"Next permutation: {permutation}")
                else:
                    print("No next permutation exists.")

            elif choice == 6:
                print("\nOption 6: Find the previous permutation in lexicographic order.")
                permutation = list(map(int, input("Enter the permutation (space-separated): ").split()))
                if previous_permutation(permutation):
                    print(f"Previous permutation: {permutation}")
                else:
                    print("No previous permutation exists.")

            else:
                print("Invalid choice. Please choose a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number or 'exit' to quit.")

if __name__ == "__main__":
    main()

