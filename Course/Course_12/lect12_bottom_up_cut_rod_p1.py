
def bottom_up(p, n):
    r = [-1] * (n+1)
    s = [-1] * (n+1)
    r[0] = 0
    for i in range(1, n+1):
        q = -1
        for j in range(1, i+1):
            val = p[j] + r[i-j]
            if val > q:
                q = val
                s[i] = j
        r[i] = q
    return r, s

def print_res(p, n):
    r, s = bottom_up(p, n)
    for i in range(1, n+1):
        print("%d, %d, %d"%(i,r[i],s[i]))


p = [0, 1, 5, 8, 9, 10, 17, 17, 20]
print_res(p, len(p)-1)