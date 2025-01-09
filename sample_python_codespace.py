f = [1,1]
for i in range(50):
    fnext = f[i]+f[i-1]
    f.append(fnext)
    print(fnext)
