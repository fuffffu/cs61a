def hailstone(n):
    if n %2==0:
        yield hailstone(n/2)
    else:
        if n!=1:
            yield hailstone(n*3+1)
        else:
            yield list(hailstone(n))

    yield n
    if n == 1:
        yield from hailstone(n)
    elif n % 2 == 0:
        yield from hailstone(n // 2)
    else:
        yield from hailstone(n * 3 + 1)

def merge(a,b):
    def sequence(start,step):
        while True:
            yield start
            start+=step

    yield ([sorted(sequence(a)+sequence(b)) for _ in range(10)])

def yield_path(t,value):
    if label(t) == value:
        yield [label(t)]
    for b in branches(t):
        for _ in  :
            yield [label(t)]+yield_path(t)