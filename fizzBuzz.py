def fizzbuzz(n):
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            res.append('fizz')
        elif i % 5 == 0:
            res.append('buzz')
        elif (i % 3 == 0) and (i % 5 == 0):
            res.append('fizzBuzz')
        else:
            res.append(i)
    return res
