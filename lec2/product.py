def product(n, term):
    result= 1
    for i in range(1, n + 1):
        result *= term(i)
    print(result)