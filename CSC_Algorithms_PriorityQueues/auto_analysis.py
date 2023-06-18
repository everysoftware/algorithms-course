from sets import TreeSet


def auto_analysis(n, e, d, equals, not_equals):
    s = TreeSet(n)
    for i in range(1, n + 1):
        s.make_set(i)
    for i in range(e):
        s.union(equals[i][0], equals[i][1])
    for i in range(d):
        if s.find(not_equals[i][0]) == s.find(not_equals[i][1]):
            return False
    return True
