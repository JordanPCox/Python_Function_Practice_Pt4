def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(max_num(3, 6, 9))
print(max_num(11, 824, 2))
print(max_num(7, 17, 77))