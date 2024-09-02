def d_to_b(values):
    remainder = []
    while values > 0:
        a = values % 2
        remainder.append(a)
        values = values // 2
    remainder.reverse()
    return ''.join(map(str, remainder))


values = int(input("enter decimal value"))
print(d_to_b(values))
