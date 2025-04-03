def memoized_cut_rod(p, n):
    r = [-1] * (n+1)
    return recursion(p,n,r)

def recursion(p,n,r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        return 0
    elif n >= 1:
        q = float('-inf')
        for i in range(1,n+1):
            q = max(q,p[i] + recursion(p,n-i,r))
    r[n] = q
    print("%d : %d"%(n, r[n]))
    return q


p = [0, 1, 5, 8, 9, 10, 17, 17, 20]
n = len(p)-1
print(memoized_cut_rod(p,n))
