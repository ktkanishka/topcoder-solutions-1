class ABCPath(object):
    def length(self, grid):
        print construct_graph(grid)

#This constructs the graph. Not we need to find the longest path within this graph.
def construct_graph(grid):
    graph = {(i, j):[] for i in range(len(grid)) for j in range(len(grid[0]))}
    for i in xrange(len(grid)):
        for j in xrange(len(grid)):
            surrounding_elements = [(l, m) for l in range(max(i - 1, 0), min(i + 2, len(grid))) for m in range(max(j - 1, 0), min(j + 2, len(grid[0])))]
            for n, k in surrounding_elements:
                if ord(grid[i][j]) == ord(grid[n][k]) - 1:
                    graph[(i, j)].append((n,k))
    return graph
