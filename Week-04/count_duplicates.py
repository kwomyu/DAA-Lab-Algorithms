def count_duplicates(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return "YES"
    return "NO"


T = int(input())
while T > 0:
    n = int(input())
    arr = list(map(int, input().split()))

    print(count_duplicates(arr))

    T -= 1
