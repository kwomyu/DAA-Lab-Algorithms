def count_pairs_with_difference(arr, k):
    arr.sort()
    count = 0
    i, j = 0, 1
    n = len(arr)

    while j < n:
        diff = arr[j] - arr[i]

        if diff == k:
            count += 1
            i += 1
            j += 1
        elif diff < k:
            j += 1
        else:
            i += 1

        if i == j:
            j += 1

    return count


# Main code
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    print(count_pairs_with_difference(arr, k))
