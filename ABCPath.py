from collections import deque

class ABCPath(object):
    def length(self, grid):
        graph = construct_graph(grid)
        in_degree_array = {i:0 for i in graph.keys()}
        for k, l in graph.iteritems():
            for v in l:
                in_degree_array[v] += 1
        q = deque([i for i in in_degree_array.keys() if in_degree_array[i] == 0])
        topological_sort = []
        while q:
            e = q.popleft()
            topological_sort.append(e)
            for v in graph[e]:
                in_degree_array[v] -= 1
                if in_degree_array[v] == 0:
                    q.append(v)
        print topological_sort
        print in_degree_array

'''
:returns: `dict`
'''
def construct_graph(grid):
    graph = {(i, j):[] for i in range(len(grid)) for j in range(len(grid[0]))}
    for i in xrange(len(grid)):
        for j in xrange(len(grid)):
            surrounding_elements = [(l, m) for l in range(max(i - 1, 0), min(i + 2, len(grid))) for m in range(max(j - 1, 0), min(j + 2, len(grid[0])))]
            for n, k in surrounding_elements:
                if ord(grid[i][j]) == ord(grid[n][k]) - 1:
                    graph[(i, j)].append((n,k))
    return graph
