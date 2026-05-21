#Duplicate in Window of Size K
def dup_window(arr, k):

    s = set()

    for i in range(len(arr)):

        if arr[i] in s:

            return True

        s.add(arr[i])

        if len(s) > k:

            s.remove(arr[i - k])

    return False

How it works: Maintains a sliding window of size k using a set; returns True if any duplicate exists within the window. Time: O(n) · Space: O(k)
