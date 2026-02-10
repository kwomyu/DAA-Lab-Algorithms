def find_three_sum_indices(arr):
    n = len(arr)

    for k in range(n):
        i = 0
        j = k - 1

        while i < j:
            current_sum = arr[i] + arr[j]

            if current_sum == arr[k]:
                return i, j, k
            elif current_sum < arr[k]:
                i += 1
            else:
                j -= 1

    return None


# Main code
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    result = find_three_sum_indices(arr)
    if result:
        i, j, k = result
        print(i, j, k)
    else:
        print("No sequence found")
