for a in range(0,1000):
    for b in range(a,1000):
        c = 1000 - b - a
        if c:
            if c**2 == a**2 + b**2:
                print(a*b*c)
