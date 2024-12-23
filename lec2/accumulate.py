def accumulate(fuse, start, n, term):
    result = start
    if n == 0:
        return (f"{start} (fuse is never used)")
    else:
        for i in range(1, n + 1):
            result = fuse(result, term(i))
        return (result)


def summation_using_accumulate(n, term):
    result = 0
    for i in range(1, n + 1):
        result += term(n)
    return result

def product_using_accumulate(n, term):
    result = 0
    for i in range(1, n + 1):
        result *= term(n)
    return result