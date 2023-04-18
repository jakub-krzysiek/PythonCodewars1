def digitize(n):
    res = [int(x) for x in str(n)[::-1]]
    return res
