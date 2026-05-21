#Nth Ugly Number
def ugly(n):

    u = [1] * n

    i2 = i3 = i5 = 0

    for i in range(1, n):

        u[i] = min(u[i2] * 2, u[i3] * 3, u[i5] * 5)

        if u[i] == u[i2] * 2: i2 += 1

        if u[i] == u[i3] * 3: i3 += 1

        if u[i] == u[i5] * 5: i5 += 1

    return u[-1]

How it works: Generates ugly numbers in order using three pointers for multiples of 2, 3, and 5. Time: O(n) · Space: O(n)
