def test(x, y, z):
    print(x, y, z)

l = [1, 2, 3]
d = {'x': 1, 'y': 2, 'z': 3}

test(*l)
test(**d)


d = {'sum': lambda x, y: x + y,
     'sub': lambda x, y: x * y}


print(d['sum'](1, 2))