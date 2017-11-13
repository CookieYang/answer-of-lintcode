def happyNum(n):
    d = {}
    while True:
        d[n] = 1
        n = sum([int(x) * int(x) for x in list(str(n))])
        if n == 1 or n in d:
            break
    return n == 1

def fun(n):
    import math
    x = math.factorial(n)
    return str(x)

print(fun(20))


