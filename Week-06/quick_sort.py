def quick_sort_with_metrics(arr, low, high, metrics):
    if low < high:
        # Partition the array and get the pivot index
        p_index = partition(arr, low, high, metrics)
        
        # Separately sort elements before and after partition
        quick_sort_with_metrics(arr, low, p_index - 1, metrics)
        quick_sort_with_metrics(arr, p_index + 1, high, metrics)

def partition(arr, low, high, metrics):
    # Choosing the last element as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        # Every iteration of this loop is a comparison with the pivot
        metrics['comparisons'] += 1
        
        if arr[j] <= pivot:
            i += 1
            # Swap elements
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                metrics['swaps'] += 1
    
    # Final swap to put the pivot in its correct place
    if (i + 1) != high:
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        metrics['swaps'] += 1
        
    return i + 1

# Example usage:
data = [10, 7, 8, 9, 1, 5]
stats = {'comparisons': 0, 'swaps': 0}

print(f"Original: {data}")
quick_sort_with_metrics(data, 0, len(data) - 1, stats)

print(f"Sorted:   {data}")
print(f"Total Comparisons: {stats['comparisons']}")
print(f"Total Swaps:       {stats['swaps']}")
