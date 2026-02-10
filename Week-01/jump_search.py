#Time Complexity: O(√n)
#Space Complexity: O(1)

from math import sqrt

def jump_search(arr, key):
    n = len(arr)
    step = int(sqrt(n))
    comparisons = 0
    prev = 0

    # 1. Jumping Phase
    while prev < n and arr[min(step, n) - 1] < key:
        comparisons += 1
        prev = step
        step += int(sqrt(n))
        if prev >= n:
            return -1, comparisons

    # 2. Linear Search Phase
    while prev < min(step, n):
        comparisons += 1
        if arr[prev] == key:
            return prev, comparisons
        prev += 1

    return -1, comparisons

user_input = input("Enter SORTED numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]

key = int(input("Enter the number to search for: "))

index, count = jump_search(arr, key)

if index != -1:
    print(f"{key} was found at index {index} after {count} comparisons.")
else:
    print(f"'{key}' was not found in the list.")
