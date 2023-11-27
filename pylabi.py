import math


def int_prysms(f, a, b, n, mt=1 / 2):
    m = n // 2
    h = (b - a) / m
    s1 = 0
    x = a + mt * h
    for k in range(m):
        s1 = s1 + h * f(x)
        x += h
    h = (b - a) / n
    s2 = 0
    x = a + mt * h
    for k in range(n):
        s2 = s2 + h * f(x)
        x += h
    d = abs(s2 - s1) / 3
    return s2, d


def f(x):
    return math.sqrt(x) * math.cos(x**2)


integral, pogresh = int_prysms(f, 0.4, 1.2, 200)
print("s_integral =", "%f" % integral, "\tpogresh =", "%f" % pogresh)

integral, pogresh = int_prysms(f, 0.4, 1.2, 200, 0)
print("l_integral =", "%f" % integral, "\tpogresh =", "%f" % pogresh)

integral, pogresh = int_prysms(f, 0.4, 1.2, 200, 1)
print("p_integral =", "%f" % integral, "\tpogresh =", "%f" % pogresh)
