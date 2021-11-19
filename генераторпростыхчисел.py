def Prime(n):
    a = 1
    ch = False
    while a != n:
        for x in range(2, a+1):
            if a % x == 0:
                ch = False
                if x == a:
                    ch = True
                break
        if ch:
            yield a
            a += 1
        else:
            a += 1

prime = Prime(30)
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
