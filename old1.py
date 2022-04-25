
b = 1729
x = 0
ss = [b]
while x != 33:
    for x in range(1, 34):
        for y in range(1, 34):
            for z in range(1,34):
                for t in range(1, 34):
                    for r in range(1, 34):
                        if (x**3 + y**3) == (z**3+t**3):
                            if x != y and x != z and x != t and y != z and y != t and z != t:
                                a = (x ** 3 + y ** 3)
                                if a != b:
                                    if a not in ss:
                                        ss.append(a)
                                        ss.sort()
                                        b = a
print(ss)