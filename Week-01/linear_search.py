#Time Complexity: O(n)
#Space Complexity: O(1)

def linear_search(arr, key):
    #Performs linear search and counts comparisons.
    comparisons = 0
    found_index = -1

    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            found_index = i
            break

    return found_index, comparisons


# Get user input
user_input = input("Enter elements separated by spaces: ")
arr = user_input.split()

key = input("Enter the element to search for: ")

index, count = linear_search(arr, key)


if index != -1:
    print(f"{key} was found at index {index} after {count} comparisons.")
else:
    print(f"'{key}' was not found in the list.")
