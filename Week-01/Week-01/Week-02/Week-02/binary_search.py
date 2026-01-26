#Time Complexity: O(log n)
#Space Complexity: O(1)

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        # Check if key is present at mid
        if arr[mid] == key:
            return mid, comparisons
        
        # If key is greater, ignore left half
        elif arr[mid] < key:
            low = mid + 1
            
        # If key is smaller, ignore right half
        else:
            high = mid - 1

    return -1, comparisons

user_input = input("Enter SORTED numbers separated by spaces: ")
arr = [int(x) for x in user_input.split()]

key = int(input("Enter the number to search for: "))

index, count = binary_search(arr, key)

if index != -1:
    print(f"{key} was found at index {index} after {count} comparisons.")
else:
    print(f"'{key}' was not found in the list after {count} comparisons.")
