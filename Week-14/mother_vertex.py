#Mother Vertex in a Graph
def dfs(graph, v, vis):

    vis[v] = True

    for i in range(len(graph)):

        if graph[v][i] == 1 and not vis[i]:

            dfs(graph, i, vis)


def mother(graph):

    n = len(graph)

    vis = [False] * n

    last = 0

    for i in range(n):

        if not vis[i]:

            dfs(graph, i, vis)

            last = i

    vis = [False] * n

    dfs(graph, last, vis)

    return last if all(vis) else -1

How it works: Uses Kosaraju's idea — the last vertex to finish DFS on the full graph is a candidate; verify by checking if it can reach all other vertices. Time: O(V + E) · Space: O(V)




