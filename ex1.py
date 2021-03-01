def ruler(n):
    line1 = ""
    line2 = ""
    i = 1
    w = 1
    count = 0
    while i <= n:
        r = i % 10
        line2 += str(r)
        if line2[-1] == '0':
            line1 += str(w)
            w += 1
        else:
            line1 += " "
        i = i + 1
    print(line1)
    print(line2)


ruler(5)
ruler(10)
ruler(25)
ruler(51)
ruler(80)
