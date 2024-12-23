def make_repeater(f, n):
    #高阶函数，函数作为参数，函数作为结果return(如果print会打印出来函数而非结果)
    def repeater(x):
        for _ in n:
            x = f(x)
        return x

    return repeater

