def pow(x, y):
    res = 1
    for i in range(y):
        res *= x
    return res


print(pow(2, 6))
