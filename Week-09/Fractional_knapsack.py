#Greedy Algorithm

Fractional Knapsack
def knapsack(w, v, W):

    items = sorted(

        [(v[i] / w[i], w[i], v[i]) for i in range(len(w))],

        reverse=True

    )

    total = 0

    for r, wt, val in items:

        if W >= wt:

            total += val

            W -= wt

        else:

            total += r * W

            break

    return total

How it works: Sorts items by value/weight ratio; greedily fills the knapsack, taking fractions when needed. Time: O(n log n) · Space: O(n)
