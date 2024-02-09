def table_union(n, m, sizes, queries):
    result = []
    s = DisjointSet(sizes)
    for i in range(m):
        s.union(queries[i][0] - 1, queries[i][1] - 1)
        print(s.maximum)
        result.append(s.curr_max)
    return result
