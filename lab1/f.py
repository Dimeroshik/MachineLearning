def s_fitness(arr):
    res = fitness(arr[0], arr[1], arr[2], arr[3])
    return res

def fitness(x, y, z, t):
    F1 = f1(x, y, z, t)
    F2 = f2(x, y, z, t)
    F3 = f3(x, y, z, t)
    F4 = f4(x, y, z, t)
    res = F1**2 + F2**2 + F3**2 + F4**2 + 1
    return res

def f1(x, y, z, t):
    return x*x + y*y - 2

def f2(x, y, z, t):
    return x + y + z + 2*t - 5

def f3(x, y, z, t):
    return x - y - z + t

def f4(x, y, z, t):
    return x + 2*y + z + t - 5