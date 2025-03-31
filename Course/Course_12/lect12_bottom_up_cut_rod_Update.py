
def bottom_up(p, n):
    r = [-1] * (n+1)
    r[0] = 0
    for i in range(1, n+1):
        q = -1
        for j in range(1, i+1):
            q = max(q, r[i-j] + p[j])
        r[i] = q
    return r

def print_res(p, n):
    r = bottom_up(p, n)
    for i in range(1, n+1):
        print("%d, %d"%(i,r[i]))


p = [0, 1, 5, 8, 9, 10, 17, 17, 20]
print_res(p, len(p)-1)