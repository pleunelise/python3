def gen(n):
    n += 1
    d = {}
    for i in range(n):
        d[i] = i*i
    print(d)
gen(5)
