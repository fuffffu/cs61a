
def a_plus_abs_b(a, b):
    if b < 0:
        f=subtract
    else:
        f = add
    return f(a, b)
