def merge_sort_with_metrics(arr, metrics):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort_with_metrics(arr[:mid], metrics)
    right_half = merge_sort_with_metrics(arr[mid:], metrics)

    return merge_and_count(left_half, right_half, metrics)

def merge_and_count(left, right, metrics):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Increment comparisons every time we enter this check
        metrics['comparisons'] += 1
        
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            # If the right element is smaller, it's an inversion
            # with ALL remaining elements in the left half
            sorted_list.append(right[j])
            metrics['inversions'] += (len(left) - i)
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Initialise metrics
my_list = [8, 4, 2, 1]
stats = {'comparisons': 0, 'inversions': 0}

sorted_arr = merge_sort_with_metrics(my_list, stats)

print(f"Original: {my_list}")
print(f"Sorted:   {sorted_arr}")
print(f"Total Comparisons: {stats['comparisons']}")
print(f"Total Inversions:  {stats['inversions']}")
