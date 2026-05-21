Minimum Spanning Tree

Prim's Algorithm
def prim(graph):

    n = len(graph)

    selected = [False] * n

    selected[0] = True

    cost = 0

    for _ in range(n - 1):

        m = float('inf')

        x = y = 0

        for i in range(n):

            if selected[i]:

                for j in range(n):

                    if not selected[j] and graph[i][j]:

                        if graph[i][j] < m:

                            m = graph[i][j]

                            x, y = i, j

        cost += m

        selected[y] = True

    return cost

How it works: Grows the MST one edge at a time by always picking the minimum-weight edge connecting the tree to an unvisited vertex. Time: O(V²) · Space: O(V)

